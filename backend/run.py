import argparse
import uvicorn
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Run the FastAPI application")
    parser.add_argument("-H", "--host", type=str, default="0.0.0.0", help="Host to bind the server to (default: 0.0.0.0)")
    parser.add_argument("-p", "--port", type=int, default=8080, help="Port to bind the server to (default: 8080)")
    parser.add_argument("-c", "--config", type=str, default="./config.yml", help="Path to config.yml file")
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="Enable debug mode with auto-reloading")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    os.environ['CONFIG_PATH'] = args.config
    uvicorn.run("app.main:app", host=args.host, port=args.port, reload=args.debug)
