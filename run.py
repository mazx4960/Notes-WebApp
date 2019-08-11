"""
Notes Web App
Copyright (C) 2019 DesmondTan
"""


###########
# Imports #
###########

import app
import argparse
import sys


###################
# Running the app #
###################


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('environment')
    args = parser.parse_args()

    if args.environment == 'development':
        # DEVELOPMENT (Internal-facing)
        app_instance = app.create_app()
        app_instance.run(host='127.0.0.1', port=5000)

    elif args.environment == 'production':
        # PRODUCTION (External-facing)
        app_instance = app.create_app(environment='production')
        app_instance.run(host='0.0.0.0', port=5000)

    else:
        print('Invalid option')
        print('only "development" or "production" mode')
        sys.exit(1)


if __name__ == '__main__':
    main()
