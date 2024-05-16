##### Demo Video Link
https://www.loom.com/share/be6ac6b73f1e4556a66fa2348c9b5b6f?sid=c5252ed1-5f1e-4964-8447-285b532ae445

##### Setup
1. Copy the `.env.example` file and rename it into `.env`
2. Fill in the values
```
POSTGRES_USER=example
POSTGRES_PASSWORD=example
POSTGRES_DB=example
/* For Development. On production, leave this as empty */
POSTGRES_HOST=

/* OIDC Keys */
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
LINKEDIN_CLIENT_ID=
LINKEDIN_CLIENT_SECRET=

/* For development: DEBUG=True;PROD=False */
DEBUG=False
PROD=True
```
3. When using your own keys, set these as the callback URLs:
- Google
```

http://localhost:8000/accounts/oidc/google/login/callback/

```
- LinkedIn

```

http://localhost:8000/accounts/oidc/linkedin/login/callback/

```
4. Make sure `docker` is running on your system. Run the command `make run`. This will build the project's image and its respective dependencies, plus running the containers.
5. Access the project through `http://localhost:8000`



