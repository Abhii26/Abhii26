# Fixes for your existing flagship repositories

These are documentation corrections grounded in the public source retrieved on 27 October 2026. The applications were not installed or run here. Follow each quick start from a clean clone yourself before describing it as tested.

## Facialytics: Face_Recognition/README.md

Open [the README](https://github.com/Abhii26/Face_Recognition/blob/main/README.md), click the pencil, and replace the current Getting Started section with the following. Preserve your other sections and screenshots.

````markdown
## Run locally

Prerequisites: Node.js/npm, and mkcert installed with a locally trusted development CA.

```bash
git clone https://github.com/Abhii26/Face_Recognition.git
cd Face_Recognition
npm ci
mkdir -p certs
mkcert -install
mkcert -key-file certs/create-ca-key.pem -cert-file certs/create-ca.pem localhost 127.0.0.1 ::1
node server.js
```

Open **https://localhost:4000**, allow camera access, and wait for model loading.

The server reads `certs/create-ca-key.pem` and `certs/create-ca.pem`. These must be locally generated development files; keep the private key out of Git. Port 4000 is the default unless the `PORT` environment variable overrides it.

On Windows, use Git Bash/WSL for the shell commands above, or create the `certs` folder manually and run the remaining commands from your terminal.
````

Additional edits:

1. Close the current setup code fence before subsequent headings. The replacement above includes both fence delimiters.
2. The existing unknown-user screenshot file is spelled `assets/unkownuseridentification.png`. Its current README link matches that misspelling and therefore is not inherently broken. If correcting it, rename the actual file and its Markdown reference together to `assets/unknownuseridentification.png`.
3. Rename the package metadata from the misspelled `face_recogniztion` to a lowercase npm-style name such as `facialytics` when you next update package metadata, and keep the lockfile synchronized through npm.
4. Change the `start` script to `node server.js` and add `dev: nodemon server.js` if you want an explicit development command. Update README commands only after applying that code change. The supplied quick start uses the entry point directly.
5. Resolve license intent: the README says MIT, package metadata says ISC, and the reviewed tree has no license file. Add the intended license and make the statements agree.
6. Add a brief Limitations section: browser camera permission/model loading, similarity thresholds and unknown faces, and the conditions under which the demo was tested. Age/expression/gender outputs should be described as model estimates, not verified facts.

## Shortifly: README.md

Open [the README](https://github.com/Abhii26/Shortifly/blob/main/README.md), click the pencil, and replace the current clone/run section with this:

````markdown
## Run locally

Prerequisites: Node.js/npm and a running MongoDB instance or MongoDB connection string.

```bash
git clone https://github.com/Abhii26/Shortifly.git
cd Shortifly
npm ci
```

Create a file named `.env` in the project root:

```dotenv
DB_URI=mongodb://127.0.0.1:27017/shortifly
```

Start the app:

```bash
node server.js
```

Open **http://localhost:8000**. Create a short link, open it, and check the visit record on the analytics page.

The current server uses port 8000. `DB_URI` is the variable read by the database connector. For a hosted database, replace the local example with your own connection string and keep credentials outside Git.
````

Additional edits:

1. In Project Structure, replace `app.js` with `server.js`, add the existing `database/connect.js`, and change `public/styles.css` to the actual `public/style.css`.
2. Add an `.env.example` containing the non-secret local `DB_URI` example. Ensure your actual `.env` stays ignored.
3. Close the old setup fence before Usage, Future Enhancements, and other headings. The replacement above fixes that structure.
4. Keep login, custom aliases, charts, and expiration under Planned work until implemented. They are currently future enhancements in the README.
5. Align the package `main` field with `server.js` when updating code. Consider `start: node server.js` and `dev: nodemon server.js`; regenerate/synchronize the lockfile as appropriate after package metadata changes.
6. Reconcile the MIT/ISC license mismatch and add the actual license file.
7. Test the existing Vercel link with a complete shorten → redirect → count flow before showing it as a working demo.

## Both repositories: improve reviewer confidence

- Keep one strong screenshot or short demo near the top; additional screenshots can go in a collapsible gallery.
- Explain the data flow and one meaningful design decision in plain language.
- Record the Node version you actually use for a successful clean installation.
- Add useful behavior tests before replacing the default failing `npm test` script or adding a CI badge.
- Remove stale instructions that conflict with the code. A short correct quick start is more useful than a long unverified one.
