package com.medical.utils;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import org.apache.commons.codec.binary.Base64;
import org.json.JSONObject;

public class SocketUtils {
	public static byte[] int2byte(int res) {
		  byte[] targets = new byte[4];

		  targets[0] = (byte) (res & 0xff);// 最低位 
		  targets[1] = (byte) ((res >> 8) & 0xff);// 次低位 
		  targets[2] = (byte) ((res >> 16) & 0xff);// 次高位 
		  targets[3] = (byte) (res >>> 24);// 最高位,无符号右移。 
		  return targets; 
		  } 

	  public static int byte2int(byte[] res) { 
		  // 一个byte数据左移24位变成0x??000000，再右移8位变成0x00??0000 

		  int targets = (res[0] & 0xff) | ((res[1] << 8) & 0xff00) // | 表示安位或 
		  | ((res[2] << 24) >>> 8) | (res[3] << 24); 
		  return targets; 
		  } 
	  public static byte[] bytesMerger(byte[] byte_1, byte[] byte_2) {
	        byte[] byte_3 = new byte[byte_1.length + byte_2.length];
	        System.arraycopy(byte_1, 0, byte_3, 0, byte_1.length);
	        System.arraycopy(byte_2, 0, byte_3, byte_1.length, byte_2.length);
	        return byte_3;
	    }
	  public static byte[] process_command(String command) {
		  byte [] com = command.getBytes();
		  int length_of_command = com.length;
		  byte[] msgsize = new byte[4]; 
		  msgsize = int2byte(length_of_command);
		  byte[] combine_stream = bytesMerger(msgsize,com);
		  return combine_stream;
	  }
	  public static byte[] encodeBase64File(String path) throws Exception {                                                                       
	        File  file = new File(path);                                                                                                            
	        FileInputStream inputFile = new FileInputStream(file);                                                                                  
	        byte[] buffer = new byte[(int)file.length()];                                                                                           
	        inputFile.read(buffer);                                                                                                                 
	        inputFile.close();                                                                                                                      
	        return new Base64().encode(buffer);                                                                                              
	    }   
	  public static JSONObject receive_json(DataInputStream inputStream) throws Exception
	  {
		  byte[] size_of_file = new byte[4];
		  byte[] bytes = new byte[1024];
		  inputStream.read(size_of_file);
		  int size_of_file_int =byte2int(size_of_file);
//		  System.out.println(size_of_file_int);
		  //System.out.println("get into this");
		  int sum_length = 0;
	      int length = 0;
	      StringBuilder sb = new StringBuilder();
	      byte[] storage = new byte[size_of_file_int] ;
	      int offset = 0;
		  while(sum_length < size_of_file_int) {//
	      	  length = inputStream.read(bytes);
//	      	  System.out.println(length);
	      	  sum_length = sum_length + length;
	      	  System.arraycopy(bytes, 0, storage, offset, length);
	      	  offset = offset + length;
//	      	  System.out.println(sum_length);

	        }

//		   System.out.println(sum_length);

		  String str1 = new String(storage, 0, storage.length,"UTF-8");
		  JSONObject jsonObject = new JSONObject(str1);//fixed_json_str
		  return jsonObject;
	  }
	  
	  public static String receive_file(DataInputStream inputStream) throws Exception
	  {
		  byte[] size_info_of_file = new byte[4];
		  inputStream.read(size_info_of_file);
		  int size_info_of_file_int =byte2int(size_info_of_file);
		  System.out.println(size_info_of_file_int);
		   byte[] file_name = new byte[size_info_of_file_int];
		   inputStream.read(file_name);
		  String file_name_str = new String(file_name, 0, file_name.length,"UTF-8");
		  String current_path = System.getProperty("user.dir");
		  File folder = new File(current_path+File.separatorChar+"image" );
		  if(!folder.exists())
		  { 
			  folder.mkdir();
		  }
		  File file =new File(current_path+File.separatorChar+"image" + File.separatorChar+ file_name_str);
        if(!file.exists()){
        	file.createNewFile();
        }
        byte[] size_of_file = new byte[4];
		inputStream.read(size_of_file);
		int size_of_file_int =byte2int(size_of_file);
        FileOutputStream fos = new FileOutputStream(file);
        byte[] bytes = new byte[1024];
        int sum_length = 0;
        int length = 0;
        while((length =  inputStream.read(bytes)) > 0 ) //接收数据并写入文件
        {
        	sum_length = sum_length + length;
            fos.write(bytes,0,length); 
            fos.flush();
        }

		  fos.close();
		  String path_of_file = file.getAbsolutePath().replace(File.separatorChar,'/');
		  String b_code = new String(encodeBase64File(path_of_file));
		  return b_code; 
		  
	  }

}
