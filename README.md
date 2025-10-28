# Lotka-Volterra-Time-Delay
The Lotka-Volterra equations were developed in the 1900s and are still a popular way to model predator-prey populations. The system of equations are constructed below where $x(t),y(t)$ represent populations and $\alpha, \beta, c, d$ are constants.
$$
\dot{x} = \alpha x - \beta xy
$$
$$
\dot{y} = -cy -dyx
$$
While much work has been done on this system, there has been a noticeable lack of work completed while introducing time-delays into the system. Time-delay terms can be important in modeling real-life populations as they can help model gestation age which can vary wildly by species. This project focuses on the system defined below with time-delay terms ($T$) incorporated to investigate how it affects the known stability of the standard Lotka-Volterra system.
$$
\dot{x} = \alpha x - \beta xy(t-T)
$$
$$
\dot{y} = -cy -dyx(t-T)
$$
It was found in our work, and modeled in this code, that an introduction of a time-delay term caused the system to be unstable when starting at the non-trivial equilibrium point. This work was a toy model before beginning work on a model of cancer tumors.
