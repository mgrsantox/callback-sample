### Setup guide

##### Step 1 : Install dependencies

create and acivate virtualenv then install dependencies
`$ pip install requiremets.txt`

#### Step 2 Run the local server

`$ fastapi dev main.py --port 8888`

##### Step 3 For the production

We will use [Tunnelmole](https://github.com/robbie-cahill/tunnelmole-client) to expose the local server to a public URL.

##### Install and run Tunnelmole

`$ npm install -g tunnelmole`
`$ tmole 8888`

Copy the tunnel `URL` and update it on callback URL of the planner settings.
