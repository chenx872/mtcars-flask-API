# Flask API


First as usual you will need to sync your repo to pull the new files. To run this API, change your directory to the docker folder and run:

`docker-compose up`

If it has created the localhost server correctly you will not get your prompt back. You will need to open a new terminal (be in the same directory) and run the following curl command to get a response

`curl http://localhost:5000/`

The inputs into the model are "grade", "lat", "long", "sqft_living", "waterfront" and "yr_built". We will pass these through a json formatted input through a curl POST request to the API. This is done as

`curl -H "Content-Type: application/json" -X POST -d '{"disp":150.0,"hp":90,"drat":3.4,"wt":2.80,"qsec":16}' "http://localhost:5000/predict_mpg"`

To stop your server running the API, type `ctrl-C`. As usual, check to see if you have any docker containers running using `docker container ls` and stop them through `docker container kill <container-name>`
