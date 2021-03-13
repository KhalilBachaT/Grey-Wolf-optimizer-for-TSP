
# Grey wolf optimizer implementation for Traveling salesman problem

## Table of content
* [Introduction](#introduction)
* [Description](#description)
* [Technologies](#technologies)
* [Setup](#setup)

## Introduction
A small python application which adapt a meta-heuristic called Grey Wolf Optimizer (GWO) inspired by grey wolves 
(The GWO algorithm mimics the leadership hierarchy and hunting mechanism of grey wolves in nature) to  solve the traveling salesman problem. 
It consists of finding the best path (with the minimum cost) where the salesman must pass by all the cities once and return to the start city.



this project was inspired from : https://www.sciencedirect.com/science/article/abs/pii/S0965997813001853
                                 http://pen.ius.edu.ba/index.php/pen/article/view/1462

## Description 
This project consist of 03 files:
* gwo_tsp.py, contains the main algorithm.
* functions.py, collects the used functions in the GWO implementation.
* main.py, the main file which contains the results viewing using Plotly .

## Technologies 
Project is created with:
* Python 3
* Plotly library

## Setup
To run this project, you have to:
* Run main.py (python main.py)
* Enter parameters if you want to change the default ones.
* Html page will appear where you can see the result and also select what do you want to see (all the paths, the best path, the new positions ...). 
