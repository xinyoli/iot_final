CREATE TABLE iot_test (
    id INT NOT NULL AUTO_INCREMENT, 
	channel int,
    sf int,
    time DATETIME,
    gwip varchar(255),
    gwid varchar(255),
	repeater varchar(255),
	systype int, 
	rssi FLOAT,
	snr FLOAT,
	snr_max FLOAT,
	snr_min FLOAT,
	macAddr int,
	data varchar(255),
	frameCnt int, 
	fport int,
	PRIMARY KEY(id)   
);