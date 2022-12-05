cd /root/stable-diffusion-webui
kill -9 `sudo lsof -t -i:7860`
/root/.pyenv/versions/sdweb/bin/python webui.py --ckpt=models/Stable-diffusion/model.ckpt --listen
