# Initial Learning Curve Results

Date: 2026-06-11

Dataset: MD17 ethanol, 10k subset  
Model: SchNetPack default MD17 experiment  
Validation samples: 100  
Test samples: 500  
Epochs: 10  
GPU: NVIDIA GeForce RTX 3060 Laptop GPU  

## Results

| n_train | epochs | test_energy_mae | test_energy_rmse | test_forces_mae | test_forces_rmse | test_loss |
|---:|---:|---:|---:|---:|---:|---:|
| 50 | 10 | 1.4213 | 1.8579 | 3.9876 | 5.4217 | 29.1350 |
| 100 | 10 | 1.2807 | 1.5965 | 2.8884 | 3.9451 | 15.4340 |
| 200 | 10 | 0.7284 | 0.9285 | 1.8346 | 2.5614 | 6.5036 |

## Observation

The force MAE decreases as the number of training samples increases, showing that the SchNet model learns a better molecular force field from more reference data.
