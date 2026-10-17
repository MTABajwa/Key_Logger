# Key_Logger

A conceptual, defense-focused study of keystroke-logging techniques, completed as part of the Cyber Security Internship (Month 1) at Arch Technologies. This write-up explains how keyloggers work, the risks they pose, and how they are detected and mitigated — it does not include a runnable keystroke-capture tool.

## Objective

To understand how keystroke-logging attacks work at a technical level and the security risks they represent, as a foundation for building detection and defensive strategies.

## What Is a Keylogger

A keylogger is any mechanism — software or hardware — that records keystrokes made on a device, typically without the user's knowledge. Limited legitimate uses exist (e.g. disclosed employer or parental monitoring), but keyloggers are overwhelmingly associated with credential theft and unauthorized surveillance, which is why they are classified as spyware/malware.

## Types of Keyloggers

- **Software keyloggers** — run as a background process or kernel-level hook that intercepts keyboard events system-wide.
- **Hardware keyloggers** — physical devices inserted between a keyboard and a computer, or embedded in keyboard firmware.
- **Form-grabbing / browser-based loggers** — capture data directly from web form submissions rather than raw key events.

## How They Work

Software keyloggers typically register a low-level hook with the operating system's input subsystem so that keyboard events pass through the logging code before (or alongside) reaching the intended application:

- **Windows** — commonly via API hooks such as `SetWindowsHookEx`.
- **Linux** — via reading raw input device events under `/dev/input`, or via X11/Wayland input APIs.

Captured keystrokes are usually buffered and written to a local file, then periodically exfiltrated — historically via email, FTP, or a command-and-control server.

## Risks & Real-World Impact

- **Credential theft** — usernames, passwords, and banking details typed by the victim can be captured in plaintext.
- **Delivery vectors** — most real-world keyloggers arrive via phishing emails, malicious attachments, trojanized downloads, or infected USB drives.
- **Persistence** — many keyloggers install themselves to survive reboots and attempt to evade antivirus detection.
- **Downstream harm** — stolen credentials are frequently resold or used for account takeover, financial fraud, and lateral movement within a network.

## Detection & Defense

- **Endpoint protection (EDR/AV)** — behavioral heuristics flag processes that hook keyboard input or write unusual data to disk.
- **Least privilege** — restricting admin rights limits a keylogger's ability to install kernel-level hooks.
- **Application allow-listing** — prevents unapproved executables from running at all.
- **On-screen/virtual keyboards** — used for sensitive fields (e.g. online banking) to defeat basic hardware/software keyloggers.
- **Multi-factor authentication (MFA)** — limits damage even if a password is captured, since a second factor is still required.
- **User awareness training** — reduces phishing click-through rates, the dominant delivery method.


## Author

**Muhammad Taimoor Afzal**
