from fastapi import FastAPI, Path

app = FastAPI()
"""
There are also validation options for string values, which are based on the length and 
use of a regular expression. In the following example, we want to define a path parameters
that accepts license plates in the form AB-123-CD. The first approach would be to force the 
string to be of length 9"""

@app.get('/license-plates/{license}')
async  def get_license_plate(license: str = Path(
    ...,
    regex = r"^\w{2}-\d{3}-\w{2}$"
)):
    return {"license": license}