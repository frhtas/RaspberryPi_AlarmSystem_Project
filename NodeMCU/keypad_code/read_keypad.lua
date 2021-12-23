id  = 0
sda = 2
scl = 1
keypad_i2c_addr=0x20
--

col_mapping_addr = 0xF0 -- row count none 240,1 224,2 208,3 176
                   --                    4 224,5 208, 6 176
                   --                    7 224,8 208, 9 176
                   --                    * 224,0 208, # 176

row_mapping_addr = 0x0F -- column count none 15 ,1 14,2 14,3 14
		      --                      ,4 13,5 13,6 13
		      --		      ,7 11,8 11,9 11
--
column_list = {[240]=false,[224]="1",[208]="2",[176]="3"}
row_list = {[15]=false,[14]="1",[13]="2",[11]="3"}
print(column_list[0])

-- initialize i2c, set pin 1 as sda, set pin 2 as scl
i2c.setup(id, sda, scl, i2c.FAST)

-- user defined function: read 1 byte of data from device
function read_reg(id, dev_addr, reg_addr)
    i2c.start(id)
    i2c.address(id, dev_addr, i2c.TRANSMITTER)
    i2c.write(id, reg_addr)
    i2c.stop(id)
    i2c.start(id)
    a = i2c.address(id, dev_addr, i2c.RECEIVER)
    print(a)    
    c = i2c.read(id, 1)
    i2c.stop(id)
    return c
end

-- get content of register 0xAA of device 0x77
row = read_reg(id, keypad_i2c_addr, row_mapping_addr)
col = read_reg(id, keypad_i2c_addr, col_mapping_addr)

-- bunların byte karşılaştırması daha sonra bakılacak
row_str_val = string.byte(row)
col_str_val = string.byte(col)

if (row_list[row_str_val] == false and column_list[col_str_val] == false) then
	print("there is no button press")
else 
	print(tonumber((row_list[row_str_val]-1)*3 +  (column_list[col_str_val]) )) 
end



