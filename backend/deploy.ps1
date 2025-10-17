function Green {
    process {
        Write-Host $_ -ForegroundColor Green
    }
}

function Red {
    process {
        Write-Host $_ -ForegroundColor Red
    }
}



Write-Output "backup start" | Red
#ssh -i ~/Documents/keys/120.79.152.79  root@120.79.152.79 '/data/aula/backup.sh'
#scp -r -P 22 -i ~/Documents/keys/120.79.152.79 etc/backup.sh root@120.79.152.79:/data/aula/
Write-Output "backup end" | Green

Write-Output "copy panel" | Red
scp -r -P 22 -i ~/Documents/keys/120.79.152.79 ./* root@120.79.152.79:/data/hubx/panel
Write-Output "copy panel done" | Green

# scp -P 22 -i ~/Documents/keys/120.79.152.79 dist.zip root@120.79.152.79:/data/nginx/aula
# ssh -i ~/Documents/keys/120.79.152.79  root@120.79.152.79 '/data/aula/deploy.sh'
