# Instructions for running

## Configuring the application
modify the .env file to point to the backend
```
VITE_BASE_URL=http://localhost:8080
```


## Running locally
```
npm i
npm run dev
```

## Running in a container
The dockerfile builds and serves the frontend in two stages, first building with a node image and then serving with an nginx image.

```
docker build -t loan-application-frontend .
docker run -p 5173:80 loan-application-frontend
```

The application will run on http://localhost:5173

