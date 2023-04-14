# need to config
name=test
home_dir=/data/
image=centos:python3.8

#启动docker，后台运行
#docker run -d -p 8080:8080 --name ${name}  -v ${home_dir}:/data -ti ${image}
#启动docker，但不运行，进入交互界面
docker run -p 8080:8080 --name ${name} -v ${home_dir}:/data -ti ${image} bash
