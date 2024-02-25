server {
        listen ${LISTEN-PORT};
        location /static {
                alias /vol/static;
        }
        location /{
            uwsgi_pass
        }

}