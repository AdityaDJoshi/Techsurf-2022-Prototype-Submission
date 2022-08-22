# Techsurf-2022-Prototype-Submission
## _The ultimate image compression tool_

This flask based tool is a web-ready python based tool to perform image compression  while maintaining the size ratio of the image. There are four files to evaluate in this repository.
## Features
- The flask app named app.py
- The compression algorithm named sample_file.py
- The python notebook PCA_analysis.ipynb to demonstrate how to reduce the number of colour channels to 30% of original
- The file called image_score.py is used seperately to perform automatic image quality assessment giving the brisque score of the image.


## Getting Started
To begin runnning these files create a virtual environment using either Conda or virtualenv. Following this install the requirement modules mentioned in *requirements.txt*.

Once done, run the flask app and verify the port to whatever is displayed in the CLI. In this example, we simply map port 8000 of the host to the flaskapp.

```sh
python app.py
```
> Note: Or alternatively

```sh
flask run
```
Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://localhost:8000
```

#### The results of the PCA analysis tool are incomplete
The output of the PCA tool is going to have white borders around it but will have 30% of the colours and will offer drastic drop in file size over the default methods approach used in com.py.

The score.py is meant to be used seperately from the flask tool. This is done so as to improve the overall responsiveness of the tool. The scoring mechanism takes on average 120 seconds to score the images based on their quality. The score ranges from 0-100 0 being the best. When performed on the image compressed by com.py the image score goes from 19 to 22. 

Lastly the pca analysis is meant to demonstrate the intermediate outputs of the principal component analysis done on one particular image.

The Processed images folder contains already processed images with outputs of the algorithm present in it.

