[0;1;32m●[0m apache2.service - The Apache HTTP Server
     Loaded: loaded (]8;;file://Jose/lib/systemd/system/apache2.service/lib/systemd/system/apache2.service]8;;; [0;1;32menabled[0m; preset: [0;1;32menabled[0m)
     Active: [0;1;32mactive (running)[0m since Thu 2024-10-10 11:01:48 CEST; 1h 8min ago
       Docs: ]8;;https://httpd.apache.org/docs/2.4/https://httpd.apache.org/docs/2.4/]8;;
    Process: 670 ExecStart=/usr/sbin/apachectl start (code=exited, status=0/SUCCESS)
   Main PID: 791 (apache2)
      Tasks: 6 (limit: 4621)
     Memory: 24.2M
        CPU: 2.202s
     CGroup: /system.slice/apache2.service
             ├─[0;38;5;245m791 /usr/sbin/apache2 -k start[0m
             ├─[0;38;5;245m844 /usr/sbin/apache2 -k start[0m
             ├─[0;38;5;245m848 /usr/sbin/apache2 -k start[0m
             ├─[0;38;5;245m849 /usr/sbin/apache2 -k start[0m
             ├─[0;38;5;245m851 /usr/sbin/apache2 -k start[0m
             └─[0;38;5;245m852 /usr/sbin/apache2 -k start[0m

Warning: some journal files were not opened due to insufficient permissions.
