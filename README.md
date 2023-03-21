# q-lipa API

[![Github Issues](https://img.shields.io/github/issues-raw/Njoguu/qlipa-API)](https://github.com/Njoguu/qlipa-API/issues) 
[![Github pull requests](https://img.shields.io/github/issues-pr-raw/Njoguu/qlipa-API?color=yellow)](https://github.com/Njoguu/qlipa-API/pulls) <br>
[![Build](https://github.com/Njoguu/qlipa-API/actions/workflows/build.yml/badge.svg?branch=main&event=push)](https://github.com/Njoguu/qlipa-API/actions/workflows/build.yml)

The Q-Lipa API is a backend service that provides data and handles the logic for Q-Lipa. This API is built with Python(FastAPI), PostgreSQL, and Firebase.

## Features
The Q-Lipa API offers the following features:

- **User management & authentication**: This handles the user data. Authenticate users who interact with the app to ensure that only authorized users can access the data and perform actions.
- **PSV Owner management & Authentication**: Allows matatu owners who have been registered to create, edit, and delete their accounts and associated data, such as PSV names, descriptions, and routes data. 
- **PSV SACCO**: Provide data about a specific registered PSV SACCO. The data will include a unique identifier, fare amount, route selected.
- **Transaction history**: Allow users to view their transaction history, including details such as transaction IDs, merchant names, transaction amounts, and timestamps.
- **Notification system**: Notify users of successful or failed transactions via SMS, email, or push notifications.
- **Security and compliance**: Implement security measures such as encryption, authentication, and authorization to protect user data and comply with relevant regulations and standards.

## Endpoints

![images](https://user-images.githubusercontent.com/60213982/224079894-df3edad3-cea7-45c4-9c3b-5017926a54b2.png)

## API Documentation
### Interactive API docs
Navigate to `/docs` to view details on the available endpoints, request and response formats, and authentication requirements. 
You will see the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)).

### Alternative API docs
Navigate to `/redoc`.
You will see the alternative automatic documentation (provided by [ReDoc](https://github.com/Rebilly/ReDoc)).

## Development
### Setup & Installtion
Clone the repository using the following command.
`git clone https://github.com/Njoguu/qlipa-API.git`

#### Running The App: with Docker
1. Make sure you have docker installed.
2. Navigate to the folder structure then build the container with the command
`docker build -t <your-image-name> .`
3. Run the container with the command
`docker run -d -p 8000:8000 <your-image-name>`

#### Running The App: 
1. The first step is to install [FastAPI](https://fastapi.tiangolo.com/). 
`pip install fastapi`
2. Install `uvicorn` to work as the server:
`pip install "uvicorn[standard]"`
3. Install all other dependencies in the requirements.txt file

### To view the app
Go to http://127.0.0.1:8000/docs

## Contributing
Contributions to the Q-Lipa API are welcome! To contribute, please follow these steps:

- Fork the repository.
- Create a new branch: ` git checkout -b my-feature-branch `
- Make changes and commit them: `git commit -m 'Add new feature'`
- Push to the branch: `git push origin my-feature-branch`
- Create a pull request.

## License
The Q-Lipa API is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/Njoguu/qlipa-API/blob/main/LICENSE) file for more information.
