# nginxPythonOnWindows
How to set up nginx + Python Flask on windows

1. Download nginx from http://nginx.org/en/download.html, select "Stable version"
2. Extract the downloaded zip file
3. Execute "pip install flask" in windows command prompt to install Flask package
4. Add the "location /api" section of sample.conf to nginx_folder\conf\nginx.conf to enable proxy_pass setting
5. Copy stop.bat and restart.bat to nginx_folder, these files are for stoppign and restarting nginx since there's no such file came with the downloaded nginx zip file
6. Execute "python test.py" to start the Flask web server listening on port 8000
7. Click "nginx.exe" of nginx_folder to start nginx web service
8. Visit http://127.0.0.1/, http://127.0.0.1/api/ and http://127.0.0.1/api/new to check out the response of nginx and Flask
