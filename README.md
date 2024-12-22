Project Plan and Scope

For this project, I am creating an automated script that will check Windows system files to ensure that important files have not been compromised/modified while also clearing the temporary files stored within Windows in the TEMP folder. This will ensure that important Windows files have not been altered and potentially malicious files being stored in the TEMP folder are removed.
	Monitoring important system files and clearing the temporary files stored within Windows is crucial to ensuring a secure system. Important Windows files can be modified by attackers which can lead to system instability or malicious activity including data exfiltration or unauthorized changes in the security settings resulting in weaker security. Tracking these changes can provide the insight needed to identify potential threats and address them accordingly (Cubarney, 2024). There are many files within a Windows files system so it is important to recognize the core areas you want to monitor such as System 32 and Program Files (Tittel, 2019). Other files can easily be added to the monitor list as needed.
Temporary files are another location that malware tends to as most users typically do not check these files. The temporary folder that stores these files is a common place for malware to end up as these files are created by all users whenever doing any common tasks (Yacono, 2023). Temporary files can easily be cleaned and deleted from the TEMP folder in Windows however, it often gets overlooked (Logix, 2020). In later versions of Windows such as Windows 10 and 11 there is a new feature called “storage Sense” which can be configured to automatically delete your temporary files (Villinger & Belcic, 2023). While this is a great option this tool lacks the ability to track and log which files were deleted and when which can be crucial information when doing digital forensics as log analysis is an essential part of the investigation (Salvation Data, 2024).
	This project aims to provide a single Python tool that performs two functions to ensure a secure and reliable Windows system. The first function is the File Monitoring tool which will check the integrity of important Windows system files by comparing the stored hash value to the current hash value to detect any changes. If a change is detected its findings will be displayed as a desktop notification. The second function is to clear the temporary files stored in the Windows TEMP folder. This will log the files that were deleted along with the date and time on a single log that is updated every time the files are cleared. 

Timeline
Planning:
•	Determine the features that the tool will contain.
•	Identify the important files that should be checked within Windows for the integrity monitor.
Development:
•	Write a Python script that will check the current hash value compared to the stored hash value for the specified important Windows files.
•	Create a desktop notification system to alert if a modification is detected.
•	Create a Python script that will clear the temporary files stored on Windows in the TEMP folder.
•	Create a log that is automatically updated whenever a TEMP clear is run logging all files deleted along with the date and time.
Testing:
•	Test file integrity monitoring tool by creating test files and then modifying them to ensure that the tool detects the modified file and that notification is displayed.
•	Test the TEMP clearing tool to ensure that the files are being cleared and that the logging is being automatically updated and stored in one log.
Deployment:
•	Publish the working tool for all to use.

References
Cubarney, T. (2024, February 16). How To Detect File Changes in Windows Server | Blumira. Blumira.com; Blumira, Inc. https://www.blumira.com/blog/detecting-windows-server-file-changes
Logix. (2020, September 28). Did You Know? Why Malware Uses the Temp Folder. Logix Consulting Managed IT Support Services Seattle. https://logixconsulting.com/2020/09/28/did-you-know-why-malware-uses-the-temp-folder/
Salvation Data. (2024, November 28). 10 Techniques for Log File Analysis in Digital Forensics. Salvation DATA. https://www.salvationdata.com/knowledge/log-file-analysis/
Tittel, E. (2019). File Integrity Monitoring Best Practices - Logsign. Logsign. https://www.logsign.com/blog/file-integrity-monitoring-best-practices/
Villinger, S., & Belcic, I. (2023, November 29). How to Delete Temporary Files From Your Windows PC. How to Delete Temporary Files from Your Windows PC. https://www.avg.com/en/signal/top-three-ways-to-clean-temporary-files-from-your-computer
Yacono, L. (2023, February 7). 5 Places Ransomware and Malware Can Hide That You May Never Check. Www.cimcor.com. https://www.cimcor.com/blog/5-places-ransomware-and-malware-can-hide-that-you-may-never-check
