# Simulation of the spread of diseases with the help of SIRD modelling in python
This repository contains the code for the SIRD and SIRDV models used in the research paper to simulate the spread of Influenza disease in the 2012 flu strain in the U.S.
## Abstract
The aim of this paper was to perform an in-depth study on the SIRD epidemiological model, which offers a framework for analysing disease dynamics, and how it can be implemented in Python programming language. Epidemiological models have been used to study infectious diseases for a long time. Both, the SIRD and SIRDV model were implemented in python and tested using influenza statistics for the 2012 flu strain in the United States. The SIRD model uses four compartments susceptible, infected, recovered and deceased. It was verified using the calculated infection rate from real world data with a 2.4% error. The SIRDV model uses an added compartment: vaccinated. It was tested with three different vaccination rates (0.00121, 0.005, 0.05) to illustrate variations in how vaccines can prevent diseases. The inclusion of vaccines led to the susceptible population to falling rapidly. It was found that higher the vaccination rate, lower the susceptible population.

## Visualizations

### Graph generated for the SIRD model
<img width="525" height="386" alt="image" src="https://github.com/user-attachments/assets/51822b3c-1dd7-4e39-9048-a778cb25ecdf" />

### Graphs generated for the SIRDV model

#### α=0.00121
<img width="525" height="383" alt="image" src="https://github.com/user-attachments/assets/a6def2b5-6742-4aa7-bc2a-d212b89646bc" />

#### α=0.005
<img width="525" height="386" alt="image" src="https://github.com/user-attachments/assets/6b90bdc2-1f0a-4f9d-bd9d-615e17930c07" />

#### α=0.05
<img width="525" height="386" alt="image" src="https://github.com/user-attachments/assets/5bea5f8d-d2e0-4a24-9d19-43e24cc80d8d" />

## Clone this repository
```
git clone https://github.com/arthika333/sird-sirdv.git
```
