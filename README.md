# Coding Assessment
The parsing of the json file and calculation are modularize into different folders as these 
function serves very different functions. I also want to encapsulate the calculation and parsing and it makes the code more modularized for better readibility and scaliablity. From my perspective,the user seem to be for hiring manager/HR so user do not need to know the exact calculation. By just using this code, they can just query using the driver without knowing the underlying working. The score computation uses cosine similarity to determine the similarity between two vectors. 

1. To use the application, the user just need to know to run Calculation.calculate()
2. All the computation are done behidn the scene without the need for user to directly interact with them
