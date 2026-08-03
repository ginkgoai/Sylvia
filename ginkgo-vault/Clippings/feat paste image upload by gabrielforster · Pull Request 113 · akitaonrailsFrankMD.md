---
title: "feat: paste image upload by gabrielforster · Pull Request #113 · akitaonrails/FrankMD"
source: "https://github.com/akitaonrails/FrankMD/pull/113"
author:
  - "[[gabrielforster]]"
published: 2026-07-12
created: 2026-07-16
description: "What Adds handling for pasting (Ctrl/Cmd + V) images while on the editor. Users can paste an image while typing on the editor and have their"
tags:
  - "clippings"
---
## What

Adds handling for pasting (Ctrl/Cmd + V) images while on the editor. Users can paste an image while typing on the editor and have their image uploaded.

## Preview

2026-07-12.23-11-14.mp4<video src="https://private-user-images.githubusercontent.com/51389447/620615455-239a2717-fa5c-46a8-b79a-b037d41b65e6.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODQyMDUxMTYsIm5iZiI6MTc4NDIwNDgxNiwicGF0aCI6Ii81MTM4OTQ0Ny82MjA2MTU0NTUtMjM5YTI3MTctZmE1Yy00NmE4LWI3OWEtYjAzN2Q0MWI2NWU2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA3MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNzE2VDEyMjY1NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY5YTFhMGFjOWZmZDdkNjc4YTQwOGMwOTFkY2UxYTYxODk3OTk4NzhlMzk2OTI2MjczY2I1MmVkN2IxMDFiOWUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.jLFCwUiw2U4efNAhglzT-3WZ4BHjQWhWRU8zvMAKbJc" data-canonical-src="https://private-user-images.githubusercontent.com/51389447/620615455-239a2717-fa5c-46a8-b79a-b037d41b65e6.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODQyMDUxMTYsIm5iZiI6MTc4NDIwNDgxNiwicGF0aCI6Ii81MTM4OTQ0Ny82MjA2MTU0NTUtMjM5YTI3MTctZmE1Yy00NmE4LWI3OWEtYjAzN2Q0MWI2NWU2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA3MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNzE2VDEyMjY1NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY5YTFhMGFjOWZmZDdkNjc4YTQwOGMwOTFkY2UxYTYxODk3OTk4NzhlMzk2OTI2MjczY2I1MmVkN2IxMDFiOWUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.jLFCwUiw2U4efNAhglzT-3WZ4BHjQWhWRU8zvMAKbJc" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px"></video>

## Why

It's pretty common for screenshot apps to write the image into the clipboard rather than storing it in a file, so handling pasting seems like a good enhancement.  
Follows the same idea from [#112](https://github.com/akitaonrails/FrankMD/pull/112): making it easier for the user to upload media while remotely using/editing the editor.

---

## Comments

> **akitaonrails** · 2026-07-13
> 
> Shipped in **v0.5.0** — thanks again [@gabrielforster](https://github.com/gabrielforster)! This one was a pleasure to review: the `processing_image_paste` key landed in all 7 locales, you extended the parity test yourself, and routing the pasted file through the existing Drop-tab ingest (and therefore the hardened `/images/upload` path) meant zero new security surface. The MIME→extension synthesis for nameless clipboard blobs was exactly the right call.
> 
> Three small adjustments on integration ([1558a9d](https://github.com/akitaonrails/FrankMD/commit/1558a9d96c5e68e786bed4a49eeab5c045851d27)):
> 
> - Unknown image MIME types now derive an honest extension from the subtype (`image/tiff` → `.tiff`) instead of defaulting to `.png`, so the allow-list rejects them with visible feedback rather than storing a mislabeled file.
> - Explicit `event.preventDefault()` in the paste interceptor — copying an image from a web page also puts `text/html` on the clipboard, which could otherwise paste stray markup while the picker opens.
> - `openWithFile` wraps ingest in try/finally so a throwing ingest can't leave the loading overlay stuck.