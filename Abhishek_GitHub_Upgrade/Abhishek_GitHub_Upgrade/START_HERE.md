# Abhishek's GitHub upgrade

Prepared 27 October 2026. Your live account has not been changed.

The design is ready to upload to your existing **Abhii26/Abhii26** repository. It uses an original animated header, coordinated project cards, and a summary of your measured engineering work. Your latest attached resume is the authority for career details; your current public repositories are the authority for repository names and setup corrections.

## 1. Update the profile sidebar

Open [GitHub public-profile settings](https://github.com/settings/profile). Fill the fields below, then click **Update profile**.

| Field | Recommended value |
| --- | --- |
| Name | Abhishek Tiwari |
| Bio | Python Developer \| Computer Vision & Edge AI \| FastAPI, Flutter, ONNX \| Building offline-first ML apps and backends. |
| Company | Techkshetra Info Solutions Pvt. Ltd. |
| Location | Bengaluru, India |
| Website | https://www.linkedin.com/in/abhishektiwari6/ |
| Social account | https://www.linkedin.com/in/abhishektiwari6/ |
| Time zone | Asia/Kolkata; display local time if useful |

The website and social-account fields can use the same LinkedIn URL initially. Once you have a portfolio, put its URL in Website and keep LinkedIn under Social accounts.

Keep **Abhii26** as your username. It is already on your resume and project links. A username change is not needed for this redesign.

For your avatar, use a clear, tightly cropped headshot with a simple background. Test its circular crop at small sizes; keep your face away from the edge. A consistent image across GitHub and LinkedIn makes the accounts easier to recognize.

You can use your existing contact email publicly if that is your preference. The supplied README already has an email link. Your phone number is deliberately absent from the profile copy.

## 2. Install the new profile README

Your profile repository already exists: [Abhii26/Abhii26](https://github.com/Abhii26/Abhii26). You do not need to create another one.

1. Download and extract the upgrade ZIP.
2. Open the **Abhii26** folder inside it. This is the folder containing the new `README.md`, `assets`, and `projects`.
3. Visit your profile repository, stay on its `main` branch, and choose **Add file → Upload files**.
4. Drag the **contents** of that local Abhii26 folder into the upload area. Include `README.md`, the complete `assets` folder, and the complete `projects` folder.
5. Check the proposed paths. You want `README.md` and `assets/hero.gif` at the repository root. You do not want `Abhii26/README.md` nested inside the repository.
6. Commit with a message such as `Refresh profile with projects and engineering work`.
7. Open [your profile](https://github.com/Abhii26) and refresh it.

If the browser's folder upload does not preserve directories, use GitHub Desktop: clone Abhii26/Abhii26, copy the local folder's contents into the clone, inspect the diff, commit, and push. This changes your profile files; it does not require changing any other repository.

Upload only the **Abhii26** folder's contents for this step. `backup`, `repository-upgrades`, and `design-source` are supporting material, not extra profile sections.

The old profile README is included under `backup/ORIGINAL_PROFILE_README.md`. GitHub commit history also retains the previous version.

### What appears immediately

- An animated navy/cyan/violet header with a typing line and abstract vision scanner.
- Local LinkedIn and email button artwork.
- Three work highlights: 29% lower group-photo processing time; selfie recognition under 3 seconds; inference across three RTSP feeds.
- Cards for FaceAuth, Facialytics, and Shortifly.
- A focused skills section and collapsible work/education details.
- Static artwork for viewers requesting reduced motion.

The hero artwork is an illustration. It is not a live inference demo. The metrics are the measurements in your resume, not live counters.

## 3. Resolve the FaceAuth source link

FaceAuth was not among the 12 public repositories returned by GitHub during this review. It may be private, unpublished, or have a different name. The FaceAuth link embedded in your latest resume currently goes to your profile homepage rather than a specific source repository.

The new profile therefore links FaceAuth to a truthful local project note. It never sends visitors to a guessed repository URL.

1. Find your actual FaceAuth repository, or publish the personal project's source when ready.
2. Use its exact URL in the FaceAuth card link and the source link in `README.md`.
3. Remove `Public source link to be added when available` after you add the working source link.
4. Update `projects/faceauth.md` to link to the source.
5. Update the FaceAuth GitHub link in your resume and LinkedIn Featured section to the same URL.

If you create a new public repository, **FaceAuth** is a clear name. Use `repository-upgrades/FACEAUTH_README_STARTER.md` to structure its README. The template contains clearly marked fields that need your project's actual commands and environment; it is not a claim that setup has been verified.

## 4. Set the repositories visitors see first

Open [your profile](https://github.com/Abhii26), find **Popular repositories** or **Pinned**, then choose **Customize your pins**. GitHub permits up to six repositories and gists in total.

Use this order, adjusting it to the source you actually have ready:

| Priority | Repository | Why it belongs |
| --- | --- | --- |
| 1 | FaceAuth, once public and documented | Closest personal project to your current computer-vision/mobile work |
| 2 | Face_Recognition, displayed as Facialytics | Existing vision project with screenshots |
| 3 | Shortifly | Backend, database, routing, and analytics evidence |
| 4 | collabzz-task-manager, after you review it | A more recent assignment that may show application structure; code was not reviewed in this task |
| 5 | A future original FastAPI project or permitted public case study | Creates public evidence for Python/backend skills now strongest in your resume |
| 6 | Leave empty until another project earns the spot | Four strong projects are sufficient; six is a limit, not a target |

For now, pin Facialytics and Shortifly first. Do not represent a private repository as a public pin. Keep course notes and tutorial clones accessible as learning history, but prioritize original work in the pinned section.

## 5. Improve each repository's About panel

Open the repository's **Code** tab, then the gear next to **About** on the right. Add the description and topics, then save.

| Repository | Description | Suggested topics |
| --- | --- | --- |
| Abhii26 | Python, computer vision, and on-device ML — projects and engineering work by Abhishek Tiwari. | github-profile, profile-readme, python, computer-vision, edge-ai |
| Face_Recognition | Facialytics: webcam face recognition and expression analysis with Node.js, Express, and face-api.js. | face-recognition, computer-vision, face-api-js, nodejs, express, javascript |
| Shortifly | URL shortener with click counts and timestamped visit analytics, built with Node.js, Express, MongoDB, and EJS. | url-shortener, nodejs, express, mongodb, ejs, analytics |
| FaceAuth, after publishing | Offline face enrollment and authentication with Flutter, SQLite, and multi-frame liveness checks. | flutter, dart, sqlite, face-recognition, offline-first, anti-spoofing |

Your current Shortifly description says `Url Shortner Website`; the proposed description fixes the spelling and explains the backend behavior. Your public repository topics were empty when checked.

Keep the current **Face_Recognition** URL during the first update so existing links remain consistent. Its README can say **Facialytics** without renaming the repository. If you later rename it, update the profile, resume, LinkedIn, clone commands, and deployment links together.

The Shortifly About panel currently points to `https://shortifly.vercel.app`. Your resume links Facialytics to `https://facialytics.vercel.app/`. Neither deployment's functionality was tested here. Try the full user flow yourself before placing either in the new profile as a live-demo button.

## 6. Fix the project instructions before promoting them

Detailed replacements are in `repository-upgrades/EXISTING_REPOSITORY_FIXES.md`.

The main observed issues are:

- **Facialytics:** placeholder clone URL; an unclosed fenced code block; port 5000 in the README versus 4000 in `server.js`; certificate filenames/locations that do not match the server; a misspelled unknown-user screenshot filename.
- **Shortifly:** `app.js` in the README versus `server.js` in the source; `MONGODB_URL` in the README versus `DB_URI` in the database connector; an unclosed fenced code block.
- **Both:** README says MIT while package metadata says ISC and the reviewed trees contain no license file. Choose the actual license you intend, add its file, and align the wording. Do not add an MIT badge until that is done.
- **Both:** `npm test` currently exits with the default "no test specified" failure. Do not add a passing-test badge. Replace that script after you add useful tests.

These are source/documentation checks. The applications were not installed or executed in this review.

## 7. Add the optional contribution snake

The custom header already animates without GitHub Actions. The snake is an additional animation based on your real GitHub contribution graph.

1. Open [the profile repository](https://github.com/Abhii26/Abhii26).
2. Choose **Add file → Create new file**.
3. Name the file `.github/workflows/snake.yml`.
4. Paste the contents of `optional/snake.yml`, then commit on `main`.
5. Open the **Actions** tab. Enable workflows if GitHub offers that control.
6. Select **Refresh contribution snake → Run workflow**.
7. Wait for a successful run. Confirm that `assets/github-snake.svg` and `assets/github-snake-dark.svg` exist.
8. Paste `optional/SNAKE_SECTION.md` near the bottom of the profile README, then commit.

This workflow uses the repository's automatic `GITHUB_TOKEN`; you do not need to create or paste a personal access token. Its write permission is used to commit the generated images to this profile repository. It also has a daily scheduled trigger at **07:07 IST** (01:37 UTC), which you can remove if you prefer manual refreshes. Scheduled jobs may run late and GitHub can disable schedules after 60 days without repository activity; rerun/re-enable the workflow when needed.

If the job cannot push because your repository protects `main`, keep the working profile and use a branch/PR process consistent with your settings. Do not weaken branch protection just for an animation.

Only add the snake README block after the first successful run; otherwise the images will not exist yet. If you later disable the job, the last generated images remain usable.

## 8. Make the projects convincing

For each flagship project, add these in order:

1. **A 15–30 second GIF or video link** showing one complete working flow. Capture the actual app and use your own face or opt-in demo users for vision examples.
2. **A quick start you have followed from a clean clone**, with exact versions, environment-variable names, and commands.
3. **An architecture diagram** showing where inference runs, how the backend is involved, and what is stored. Keep employer implementation details out of personal-project documentation.
4. **An evaluation or tradeoff section**: failed cases, limitations, why you chose the approach, and what you would improve next.
5. **Useful tests and CI** around actual behavior. For Shortifly, link creation, invalid input, redirect behavior, and visit counting are useful test cases. For FaceAuth, describe the test scope and limitations for enrollment, matching, and liveness.
6. **A release or reproducible demo** once you have tested the build and documented model/dependency requirements.

For FaceAuth, the demo could show enroll → disconnect network → authenticate → demonstrate a rejected attempt → inspect app state. Do not claim a print/replay attack is rejected unless you have actually tested that case.

For performance notes, record device/CPU, input size, face count, model versions, release mode, warm-up, timed stages, number of runs, and median/tail timings. Keep similarity scores separate from measured false-match/false-non-match rates.

## 9. Keep the visual system coherent

Use the same navy background, cyan/violet accents, project titles, and short descriptions across GitHub, LinkedIn Featured thumbnails, and a future portfolio.

The code-drawn assets are in `Abhii26/assets`. The editable generator is `design-source/render_assets.py`; it requires Python and Pillow. There are no remote fonts, image-stat APIs, or tracking pixels in the new core profile. The supplied artwork is intentionally legible on both GitHub themes, with text equivalents for the image content.

Do not add a wall of visitor counters, skill-percentage bars, or many overlapping animated widgets. They would make this particular design harder to read. A contribution heatmap measures activity, and a language chart measures repository composition; neither represents your overall skill level or your private professional work.

GitHub's private dashboard and navigation cannot be restyled through a profile README. You can customize the README, avatar, bio, profile fields, pins, and repository presentation. Free-form JavaScript, React components, and custom CSS are not a way to redesign the surrounding GitHub page. If you later want that level of interaction, build a separate portfolio and link it from Website.

## 10. Verify the published result

- View your profile signed out, at desktop and phone widths, in light and dark themes.
- Check the hero, buttons, project cards, and local project-note links.
- Click LinkedIn and email; the new LinkedIn URL should contain only one `/in/` segment.
- Confirm that the job title and employer are still current when you publish.
- Confirm source links and pin order. Replace the FaceAuth placeholder note only when you have the actual source URL.
- If enabled, check the snake workflow's first run and generated images.
- Read the profile in 15 seconds: a visitor should identify your role, strongest work, projects, and how to contact you.

## Suggested order of work

**First session:** update name/bio/links, install the README/assets, pin Facialytics and Shortifly, fix their setup documentation.

**Next:** publish or link FaceAuth, add a genuine demo, and replace the temporary source-availability wording.

**Then:** add one well-documented original FastAPI project or permitted case study that makes your Python backend experience visible in public code. Add the optional snake when the core profile is working.

Design research, source links, and the detailed audit are in [RESEARCH_AND_AUDIT.md](RESEARCH_AND_AUDIT.md).
