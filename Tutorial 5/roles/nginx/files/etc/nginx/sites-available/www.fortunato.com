upstream fortunato {
    server unix:/run/uwsgi/www.fortunato.com.sock;
}

server {
    listen 80;
    server_name _;

    access_log /var/log/nginx/www.fortunato.com.access.log;
    error_log /var/log/nginx/www.fortunato.com.error.log;

    root /var/www/www.fortunato.com/;

    location /static {
    }

    location / {
        include /etc/nginx/uwsgi_params;
        proxy_redirect     off;
        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;

        add_header X-Frame-Options SAMEORIGIN;

        uwsgi_pass  fortunato;
    }
}
