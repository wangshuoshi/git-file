#!/usr/bin/python
# -*- coding: latin-1 -*-

#光纤网卡和HBA卡的区别
"""
存储区域网络(Storage Area Network,简称SAN)采用网状通道(Fibre Channel,简称FC,
区别与Fiber Channel光纤通道)技术,通过FC交换机连接存储阵列和服务器主机.

早期的SAN存储系统中,服务器与交换机的数据传输是通过光纤进行的,因为服务器是把SCSI指令
传输到存储设备上,不能走普通LAN网的IP协议,所以需要使用FC传输,因此,这种SAN就叫做FC
－SAN.后来,出现了用IP协议封装的SAN,可通过LAN网络,因此,被称为IP-SAN.其中,最典型
的就是现在热门的ISCSI.

这两种方式都需要对数据块进行频繁的读包解包操作,所以高性能的SAN系统是需要在服务器上安装
一块专门负责解包工作,来减轻处理器来自网卡的负担,这种网卡称为HBA卡.HBA卡除了执行解包
工作外,当然还可以提供一个光纤接口用来跟对应的交换机连接；另外,HBA物理上可以把它当作网卡一样
插,CI或者PCI-E槽位里,因此,这种设备的用法非常像一张网卡,很多人也就把他跟普通网卡或者普通的
光纤网卡混淆.当然,有的ISCSI HBA卡就可以当作普通网卡来用,不过从价格上考虑这样非常浪费的.

因传输协议的不同的,网卡可分为三种,一是以太网卡,二是FC网卡,三是iSCSI网卡
•以太网卡：学名Ethernet Adapter,传输协议为IP协议,一般通过光纤线缆或双绞线与以太网交换机连接
•FC网卡：一般也叫光纤网卡,学名Fibre Channel HBA.传输协议为光纤通道协议.
•ISCSI网卡：学名ISCSI HBA,传输ISCSI协议,接口类型与以太网卡相同.
“光纤网卡”一般是指FC HBA卡,插在服务器上,外接存储用的光纤交换机.
HBA卡：FC-HBA卡(俗称：光纤网卡) iSCSI-HBA卡(RJ45接口)

WWN是HBA卡用的编号吧,每一个光纤通道设备都有一个唯一的标识,称为WWN(world wide name),在有多
台主机使用磁盘阵列时,通过WWN号来确定哪台主机正在使用指定的LUN(或者说是逻辑驱动器),被使用的
LUN其他主机将无法使用.
"""

#scsi
"""
Linux中的SCSI设备的命名方式能够帮助用户识别设备.例如,第一个SCSI CD-ROM是/dev/scd0.SCSI磁
盘的标签为/dev/sda /dev/sdb和/dev/sdc等.这些 SCSI 设备可能具有通用的名称和接口,比如
/dev/sg0 /dev/sg1或/dev/sga /dev/sgb等.通过这些通用的驱动器接口,您就可以将SCSI命令直接发送
到SCSI设备,而不需要经过在SCSI磁盘上创建(并装载到某个目录)的文件系统.

sg_inq -d /dev/sdb  支持那些标准的version descriptor
sg_vpd /dev/sdh  支持那些vpd
sg_scan和cat /proc/scsi/scsi

在Linux中scsi驱动基本分为三大层：top level,middle level以及lower level.在scsi middle level
定义了scsi device的数据结构,用于描述一个scsi的具体功能单元,其在scsi host中通过channel,id,lun
进行寻址.

在scsihost中可以存在多个channel,每个channel是一条完整的scsi总线,在scsi总线上可以连接
多个scsi节点,每个节点采用id进行编号.每个节点可以根据功能划分成多个lun,每个lun才是我们
通常所说的scsi设备.

#scsi host的抽象
scsi host的语义很清晰,其描述了一个scsi总线控制器.在很多实际的系统中,scsi host为一块基于
PCI总线的HBA或者为一个SCSI控制器芯片.每个scsi host可以存在多个channel,一个channel实际扩展了
一条SCSI总线.每个channel可以连接多个scsi节点,具体连接的数量与scsi总线带载能力有关.

I2C总线是由数据线SDA和时钟SCL构成的串行总线,可发送和接收数据.在CPU与被控IC之间 IC与IC之间进
行双向传输.各种被控制电路均并联在这条总线上,但就像电话机一样只有拨通各自的号码才能工作,所以每
个电路和模块都有唯一的地址,在信息的传输过程中,I2C总线上并接的每一模块电路既是主控器,又是发送器
(或接收器),这取决于它所要完成的功能.

CPU发出的控制信号分为地址码和控制量两部分,地址码用来选址,即接通需要控制的电路,确定控制的种类；
控制量决定该调整的类别(如对比度 亮度等)及需要调整的量.这样,各控制电路虽然挂在同一条总线上,
却彼此独立,互不相关.
"""

#bmc
"""
ipmitool -t 0x1e -U admin -P admin -H 192.168.188.91 power off
sensor list 显示系统所有传感器列表
fru list 显示系统所有现场可替代器件的列表
lan print 显示channel的网络配置信息
sel list 显示所有系统事件日志
Ipmitool chassis bootdev pxe
首先,PXE client端(BIOS里面的PXE固件)广播一个DHCPDISCOVER的包,它询问所需的网络配置以及网络启
动的参数.标准DHCP服务器(非PXE enabled)将回复一个普通的DHCPOFFER包,其中包含网络信息(如IP地址
),但并不能提供PXE相关参数,因此PXE Client并不能启动.而PXE enabled的DHCP服务器所回复的
DHCPOFFER包里则包含PXE相关信息.
在解析一个PXE enabled的DHCP服务器返回的DHCPOFFER包后,PXE client就能够设置自己的IP地址 IP Mask等等,
并且指向网络上的启动资源,比如TFTP服务器上的vmlinuz文件和initrd文件.
然后PXE client就通过TFTP下载这些启动资源到自己的内存中.这些启动资源其实就是最小的操作系统.这个
最小操作系统在装载了网络驱动和TCP/IP协议栈之后,就会开始boot或者install完整的操作系统了.而这个
boot或install的过程,就不再通过TFTP来做,而是通过更加健壮的网络传输协议(如HTTP,CIFS,iSCSI或
NFS)来做.而boot或者install所用到的实体,比如磁盘或者CD-ROM是位于远端的,因此需要通过网络传输协
议来做.
1. 内核引导之前的不同
普通的从硬盘启动Linux系统最初是BIOS将MBR(主引导记录)加载入内存,然后将控制权交给MBR中的
bootloader程序,bootloader程序经过几个stage的加载后,最后将vmlinuz(可引导的,压缩的内核)加载入
内存,开始内核引导.
而PXE的启动过程在内核引导之前,是由BIOS中的PXE固件开启NBP程序(比如DHCP的网络通信),然后下载
vmlinuz和initrd,之后再进入内核启动过程.
2. 内核引导之后的不同
vmlinuz和initrd运行得差不多了之后,普通的硬盘Linux启动就从本地硬盘加载/sbin/init并运行为1号进程,
以及启动系统服务等等,而PXE的启动在内核引导完成之后,仍然会通过网络的方式(但不是TFTP协议,而是其他
更加健壮的协议如NFS,iSCSI等),加载真正的完整操作系统,如/sbin/init应该就是位于网络远端的硬盘上.
"""

"""
共享内存是常用的进程间通信，两个进程可以直接共享访问同一块内存区域
"""