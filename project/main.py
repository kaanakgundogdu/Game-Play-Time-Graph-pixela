import requests

# NOTE : FILL THIS AREA WITH YOUR INFORMATIONS
USER_NAME = ""
TOKEN = ""
GRAPH_ID = ""


pixela_enpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# NOTE: For creating user. MUST RUN FIRST TIME THAN COMMENT IT
resp = requests.post(url=pixela_enpoint, json=user_params)
print(resp.text)

graph_endpoint = f"{pixela_enpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Game Play Time Graph",
    "unit": "hours",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# NOTE: FOR CREATING GRAPH RUN FIRST TIME AND THAN COMMENT IT
resp_second = requests.post(
    url=graph_endpoint, json=graph_config, headers=headers)
print(resp_second.text)


# NOTE: ADDING PIXEL TO GRAPH
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_adding_config = {
    "date": "20220605",
    "quantity": "5"
}

resp_third = requests.post(
    url=pixel_endpoint, json=pixel_adding_config, headers=headers)
print(resp_third.text)


UPDATE_DATE = 20220608
update_endpoint = f"{pixel_endpoint}/{UPDATE_DATE}"

# NOTE: UPDATE PIXEL
new_piexldata = {
    "quantity": "3"
}

# RUN WHEN YOU NEED UPDATE
# resp_forth = requests.put(
#     url=update_endpoint, json=new_piexldata, headers=headers)

# print(resp_forth.text)

# NOTE: DELETE PIXEL

# resp_fifth = requests.delete(
#     url=update_endpoint, headers=headers)

# print(resp_fifth.text)
