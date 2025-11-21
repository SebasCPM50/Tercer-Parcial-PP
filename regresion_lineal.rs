// src/main.rs
// Implementación equivalente al código Python proporcionado
use std::time::Instant;

struct LinearRegressionModel {
    w: f64,  // pendiente
    b: f64,  // intercepto
}

impl LinearRegressionModel {
    fn new() -> Self {
        LinearRegressionModel { w: 0.0, b: 0.0 }
    }

    fn train(&mut self, x: &[f64], y: &[f64], learning_rate: f64, epochs: usize, verbose: bool) -> f64 {
        let m = x.len() as f64;
        let start = Instant::now();

        for epoch in 0..epochs {
            // Predicción: y_pred = w * X + b
            let y_pred: Vec<f64> = x.iter()
                .map(|&xi| self.w * xi + self.b)
                .collect();

            // Error: error = y_pred - y
            let error: Vec<f64> = y_pred.iter()
                .zip(y.iter())
                .map(|(pred, actual)| pred - actual)
                .collect();

            // Cálculo de gradientes (derivadas parciales)
            // dw = (2/m) * sum(error * X)
            let dw: f64 = (2.0 / m) * x.iter()
                .zip(error.iter())
                .map(|(xi, ei)| xi * ei)
                .sum::<f64>();

            // db = (2/m) * sum(error)
            let db: f64 = (2.0 / m) * error.iter().sum::<f64>();

            // Actualización de parámetros
            self.w -= learning_rate * dw;
            self.b -= learning_rate * db;

            // (Opcional) Mostrar el costo cada cierto número de épocas
            if verbose && (epoch + 1) % 200 == 0 {
                let mse: f64 = error.iter()
                    .map(|e| e * e)
                    .sum::<f64>() / m;
                println!("Epoch {}, MSE: {:.4}, w: {:.4}, b: {:.4}", 
                    epoch + 1, mse, self.w, self.b);
            }
        }

        let duration = start.elapsed();
        duration.as_secs_f64()
    }

    fn predict(&self, x: f64) -> f64 {
        self.w * x + self.b
    }
}

fn generate_data(n_samples: usize, seed: u64) -> (Vec<f64>, Vec<f64>) {
    use rand::Rng;
    use rand::SeedableRng;
    use rand_chacha::ChaCha8Rng;

    let mut rng = ChaCha8Rng::seed_from_u64(seed);

    let x: Vec<f64> = (0..n_samples)
        .map(|_| rng.gen_range(-3.0..3.0))
        .collect();

    let y: Vec<f64> = x.iter()
        .map(|&xi| 2.0 * xi + 3.0 + rng.gen_range(-0.1..0.1))
        .collect();

    (x, y)
}

fn run_benchmark(n_samples: usize, n_runs: usize) {
    println!("\n### Dataset: {} muestras ###", n_samples);
    println!("{}", "-".repeat(50));

    let mut times = Vec::new();

    for run in 0..n_runs {
        let (x, y) = generate_data(n_samples, 42 + run as u64);

        let mut model = LinearRegressionModel::new();
        let train_time = model.train(&x, &y, 0.01, 1000, false);

        times.push(train_time);

        println!("Run {}: Tiempo={:.6}s, w={:.4}, b={:.4}", 
            run + 1, train_time, model.w, model.b);
    }

    // Estadísticas
    let avg_time: f64 = times.iter().sum::<f64>() / times.len() as f64;
    let variance: f64 = times.iter()
        .map(|t| (t - avg_time).powi(2))
        .sum::<f64>() / times.len() as f64;
    let std_time = variance.sqrt();

    println!("{}", "-".repeat(50));
    println!("PROMEDIO: Tiempo={:.6}s", avg_time);
    println!("DESVIACIÓN: Tiempo={:.6}s", std_time);
}

fn main() {
    println!("### EJEMPLO BÁSICO (del código original) ###");
    println!("{}", "=".repeat(70));

    // Datos de ejemplo originales
    let x = vec![1.0, 2.0, 3.0, 4.0, 5.0];
    let y = vec![2.0, 4.0, 6.0, 8.0, 10.0];

    let mut model = LinearRegressionModel::new();
    let train_time = model.train(&x, &y, 0.01, 1000, true);

    println!("\nModelo final: w={:.4}, b={:.4}", model.w, model.b);
    println!("Tiempo: {:.6}s", train_time);

    // Predicción
    let x_nuevo = 7.0;
    let y_pred = model.predict(x_nuevo);
    println!("\nPredicción para x={}: y={:.4}", x_nuevo, y_pred);

    // Benchmarks completos
    println!("\n\n### BENCHMARKS COMPLETOS ###");
    println!("{}", "=".repeat(70));

    run_benchmark(100, 5);
    run_benchmark(1000, 5);
    run_benchmark(10000, 5);
}
