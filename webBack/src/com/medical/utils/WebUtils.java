package com.medical.utils;

import java.lang.reflect.InvocationTargetException;
import java.io.BufferedReader;
import java.io.File;
import java.lang.reflect.*;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.apache.commons.beanutils.BeanUtils;

public class WebUtils {
	
	  
	 public static String readJSONString(HttpServletRequest request){
	        StringBuffer json = new StringBuffer();
	        String line = null;
	        try {
	            BufferedReader reader = request.getReader();
	            while((line = reader.readLine()) != null) {
	                json.append(line);
	            }
	        }
	        catch(Exception e) {
	            System.out.println(e.toString());
	        }
	        return json.toString();
	}
	 
	public static<T> T copyParaToBean(Map value,T bean) {
		try {
			BeanUtils.populate(bean, value);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		return bean;
	}
    public static int parseInt(String strInt,int defaultValue) {
        try {
            return Integer.parseInt(strInt);
        } catch (Exception e) {
//        	System.out.println("WebUtils����parseInt��strIntΪ"+strInt);
            e.printStackTrace();
        }
        return defaultValue;
    }

    
    public static String[] getFiledName(Object o){  
        Field[] fields=o.getClass().getDeclaredFields();  
        String[] fieldNames=new String[fields.length];  
        for(int i=0;i<fields.length;i++){  
            fieldNames[i]=fields[i].getName();  
        }  
        return fieldNames;  
    }  
    public static Object getFieldValueByName(String fieldName, Object o) {  
        try {    
            String firstLetter = fieldName.substring(0, 1).toUpperCase();    
            String getter = "get" + firstLetter + fieldName.substring(1);    
            Method method = o.getClass().getMethod(getter, new Class[] {});    
            Object value = method.invoke(o, new Object[] {});    
            return value;    
        } catch (Exception e) {    
          
            return null;    
        }    
    }
    public static Object[] getFieldValues(Object o) {
    	
		String[] fieldNames = getFiledName(o);
		Object[] allValue=new Object[fieldNames.length];
		  for(int j=0 ; j<fieldNames.length ; j++){     //������������
	               
			  String name = fieldNames[j];    //��ȡ���Ե�����
	          Object value = getFieldValueByName(name,o);
	               allValue[j]=value;
	        }
		return allValue;

    }
    public static  boolean delAllFile(String path) {  
        boolean flag = false;  
        File file = new File(path);  
        if (!file.exists()) {  
            return flag;  
        }  
        if (!file.isDirectory()) {  
            return flag;  
        }  
        String[] tempList = file.list();  
        File temp = null;  
        for (int i = 0; i < tempList.length; i++) {  
            if (path.endsWith(File.separator)) {  
                temp = new File(path + tempList[i]);  
            } else {  
                temp = new File(path + File.separator + tempList[i]);  
            }  
            if (temp.isFile()) {  
                temp.delete();  
            }  
            if (temp.isDirectory()) {  
                delAllFile(path + "/" + tempList[i]);// ��ɾ���ļ���������ļ�  
                delFolder(path + "/" + tempList[i]);// ��ɾ�����ļ���  
                flag = true;  
            }  
        }  
        return flag;  
    }  
      
    /*** 
     * ɾ���ļ��� 
     *  
     * @param folderPath�ļ�����������·�� 
     */  
    public  static void delFolder(String folderPath) {  
        try {  
            delAllFile(folderPath); // ɾ����������������  
            String filePath = folderPath;  
            filePath = filePath.toString();  
            java.io.File myFilePath = new java.io.File(filePath);  
            myFilePath.delete(); // ɾ�����ļ���  
        } catch (Exception e) {  
            e.printStackTrace();  
        }  
    }

}
