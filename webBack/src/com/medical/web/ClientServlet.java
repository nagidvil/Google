package com.medical.web;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.JSONArray;
import org.json.JSONObject;

import com.medical.socket.district_warning_function;
import com.medical.socket.get_data_function;
import com.medical.socket.statistic_function;
import com.medical.utils.WebUtils;

public class ClientServlet extends BaseServlet{
	public ClientServlet() {
        super();
        // TODO Auto-generated constructor stub
    }
	protected void getMonthResults(HttpServletRequest request, HttpServletResponse response) throws Exception {
		// TODO Auto-generated method stub
		String json = WebUtils.readJSONString(request);
		System.out.println(json);
        JSONObject jsonObject = new JSONObject(json);
		String func = jsonObject.getString("function");
		String info2python = jsonObject.getString("infoValue");
		if (func.equals("get_month2019_results")) //统计分析-》时间-》月-》2019年月份统计信息
		{
			System.out.println("2019");
			 JSONObject receipt_json = statistic_function.month2019_results_fuction();
			 System.out.println(receipt_json.toString());
			 response.getWriter().write(receipt_json.toString());
		}
		
		else if(func.equals("get_month2020_results"))//统计分析-》时间-》月-》2020年月份统计信息,2019和2020的信息要一起显示在患病时间统计那块
		{
			System.out.println("2020");
			JSONObject receipt_json = statistic_function.month2020_results_fuction();
			System.out.println(receipt_json.toString());
			 response.getWriter().write(receipt_json.toString());
		}
		else if(func.equals("get_month_results"))
		{
			System.out.println("month");
			//json_info = {'results_year': year, 'results_month': month, 'results_num': num}
			JSONObject receipt_json1 = statistic_function.month2019_results_fuction();
			JSONObject receipt_json2 = statistic_function.month2020_results_fuction();
			JSONArray jsonArray = new JSONArray(); 
			JSONObject return_ob = new JSONObject(); 
			String year1=receipt_json1.getString("results_year");
			String year2=receipt_json2.getString("results_year");
			jsonArray.put(year1);
			jsonArray.put(year2);
			return_ob.put("results_year", jsonArray);
			JSONArray jsonArray1 = new JSONArray(); 
			String month1=receipt_json1.getString("results_month");
			String month2=receipt_json2.getString("results_month");
			jsonArray.put(month1);
			jsonArray.put(month2);
			return_ob.put("results_month", jsonArray1);
			JSONArray jsonArray2 = new JSONArray(); 
			String day1=receipt_json1.getString("results_num");
			String day2=receipt_json2.getString("results_num");
			jsonArray.put(day1);
			jsonArray.put(day2);
			return_ob.put("results_day", jsonArray2);
			System.out.println(return_ob.toString());
			response.getWriter().write(return_ob.toString());
		}
		
	}
	protected void getCriticalPatient (HttpServletRequest request, HttpServletResponse response) throws Exception {
		String json = WebUtils.readJSONString(request);
		System.out.println(json);
        JSONObject jsonObject = new JSONObject(json);
		String func = jsonObject.getString("function");
		String info2python = jsonObject.getString("infoValue");
		if (func .equals("get_dan_patient")) //危急患者
		{
			 JSONObject receipt_json = district_warning_function.dan_patient_fuction();
			 System.out.println(receipt_json.toString());
			 response.getWriter().write(receipt_json.toString());
		}
		else if (func .equals("get_similar_patient")) //相似患者
		{
			 JSONObject receipt_json = district_warning_function.similar_patient_fuction(info2python);
			 response.getWriter().write(receipt_json.toString());
		}
		
	}
	protected void getWebData (HttpServletRequest request, HttpServletResponse response) throws Exception {
		String json = WebUtils.readJSONString(request);
        JSONObject jsonObject = new JSONObject(json);
		String func = jsonObject.getString("function");
		String info2python = jsonObject.getString("infoValue");
		System.out.println(info2python);
		if (func.equals("getWebData")) //获取自定义网址数据，返回json格式的年龄和疾病名
		{
			 JSONObject receipt_json = get_data_function.getWebData(info2python);
			 System.out.println(receipt_json.toString());
			 response.getWriter().write(receipt_json.toString());
		}
//		else if (func =="getWeiboData") //执行提取微博中数据的功能，无返回值
//		{
//			get_data_function.getWeiboData();
//		}
	}
	
	protected void getAllnumber (HttpServletRequest request, HttpServletResponse response) throws Exception {
		String json = WebUtils.readJSONString(request);
		System.out.println(json);
        JSONObject jsonObject = new JSONObject(json);
		String func = jsonObject.getString("function");
		String info2python = jsonObject.getString("infoValue");
		
		if (func .equals("get_age_allnumber")) //统计分析-》年龄-》累计人数
		{
			 JSONObject receipt_json = statistic_function.age_allnumber_fuction();
			 response.getWriter().write(receipt_json.toString());
		}
		if (func .equals("get_age_addnumber")) //统计分析-》年龄-》增加人数
		{
			 JSONObject receipt_json = statistic_function.age_addnumber_fuction();
			 response.getWriter().write(receipt_json.toString());
		}
		if (func .equals("get_time_allnumber")) //统计分析-》时间-》累计人数
		{
			 JSONObject receipt_json = statistic_function.time_allnumber_fuction();
			 response.getWriter().write(receipt_json.toString());
		}
		if (func .equals("get_time_addnumber")) //统计分析-》时间-》增加人数
		{
			 JSONObject receipt_json = statistic_function.time_addnumber_fuction();
			 response.getWriter().write(receipt_json.toString());
		}
		if (func .equals("get_country_allnumber")) //统计分析-》地区-》全国-》累计求助（全国累计求助）
		{
			 JSONObject receipt_json = statistic_function.country_allnumber_fuction();
			 System.out.println(receipt_json.toString());
			 response.getWriter().write(receipt_json.toString());
		}
		if (func .equals("get_country_addnumber")) //统计分析-》地区-》全国-》增加人数（全国增加求助）
		{
			 JSONObject receipt_json = statistic_function.country_addnumber_fuction();
			 System.out.println(receipt_json.toString());
			 response.getWriter().write(receipt_json.toString());
		}
		if (func .equals("get_province_allnumber")) //统计分析-》地区-》各省-》累计求助（当前省累计求助）
		{
			 JSONObject receipt_json = statistic_function.province_allnumber_fuction(info2python);//info2python是省名
			 response.getWriter().write(receipt_json.toString());
		}
		if (func .equals("get_province_addnumber")) //统计分析-》地区-》各省-》增加求助（当前省增加求助）
		{
			 JSONObject receipt_json = statistic_function.province_addnumber_fuction(info2python);//info2python是省名
			 response.getWriter().write(receipt_json.toString());
		}
		if (func .equals("get_city_allnumber")) //统计分析-》地区-》各市-》累计求助（当前市累计求助）
		{
			 JSONObject receipt_json = statistic_function.city_allnumber_fuction(info2python);//info2python是市名
			 response.getWriter().write(receipt_json.toString());
		}
		if (func .equals("get_city_addnumber")) //统计分析-》地区-》各市-》增加求助（当前市增加求助）
		{
			 JSONObject receipt_json = statistic_function.city_addnumber_fuction(info2python);//info2python是市名
			 response.getWriter().write(receipt_json.toString());
		}
		
		
	}
	/*get_age:统计分析-》年龄
	 * get_year:统计分析-》时间-》年
	 * get_day：统计分析-》时间-》日
	 * get_country：统计分析-》地区-》全国
	 * get_province：统计分析-》地区-》各省
	 * get_city：统计分析-》地区-》各市
	 * get_area：地区预警
	 * pic,picture:照片
	 * results:右侧字符显示数据栏信息
	 * */
	protected void getAllPic (HttpServletRequest request, HttpServletResponse response) throws Exception {
		String json = WebUtils.readJSONString(request);
		System.out.println(json);
        JSONObject jsonObject = new JSONObject(json);
		String func = jsonObject.getString("function");
		String info2python = jsonObject.getString("infoValue");
		//待修改
		 
		
			if(func.equals( "get_age_picture"))//统计分析-》年龄-》图片
			{
				 JSONObject receipt_json = statistic_function.age_picture_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
			else if(func.equals("get_year_picture")) //统计分析-》年龄-》图片
			{
				 JSONObject receipt_json = statistic_function.year_picture_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
			else if(func.equals("get_month2019_picture")) //2019和2020的图片同时要放在对应的放图片的区域
			{
				 JSONObject receipt_json = statistic_function.month2019_picture_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
			else if(func.equals("get_month2020_picture")) 
			{
				 JSONObject receipt_json = statistic_function.month2020_picture_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
			else if(func.equals( "get_month_picture"))
			{
				JSONObject receipt_json = statistic_function.month2020_picture_fuction();
				 response.getWriter().write(receipt_json.toString());
				
			}
			else if(func.equals("get_day_picture"))
			{
				 JSONObject receipt_json = statistic_function.day_picture_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
			else if(func.equals("get_country_picture"))
			{
				 JSONObject receipt_json = statistic_function.country_picture_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
			else if(func.equals( "get_province_picture")) 
			{
				 JSONObject receipt_json = statistic_function.province_picture_fuction(info2python);
				 response.getWriter().write(receipt_json.toString());
				 
			}
			else if( func.equals("get_city_picture")) 
			{
				 JSONObject receipt_json = statistic_function.city_picture_fuction(info2python);
				 response.getWriter().write(receipt_json.toString());
				 
			}
			//待修改
			else if(func.equals( "get_area_pic"))
			{
				JSONObject receipt_json1 = district_warning_function.area_age_pic_fuction(info2python);
				JSONObject receipt_json2 = district_warning_function.area_city_pic_fuction(info2python);
				JSONObject receipt_json3 = district_warning_function.area_month_pic_fuction(info2python);
				JSONArray jsonArray = new JSONArray(); 
				String pic1=receipt_json1.getString("picture");
				String pic2=receipt_json2.getString("picture");
				String pic3=receipt_json3.getString("picture");
				jsonArray.put(pic1);
				jsonArray.put(pic2);
				jsonArray.put(pic3);
				JSONObject return_ob = new JSONObject(); 
				return_ob.put("picture", jsonArray);
				System.out.println(return_ob.toString());
				response.getWriter().write(return_ob.toString());
				
			}

		
		
		
	}
	protected void getBasicResults (HttpServletRequest request, HttpServletResponse response) throws Exception {
		String json = WebUtils.readJSONString(request);
		System.out.println(json);
        JSONObject jsonObject = new JSONObject(json);
		String func = jsonObject.getString("function");
		String info2python = jsonObject.getString("infoValue");
		
		    if(func.equals("get_age_results")) 
			{
				 JSONObject receipt_json = statistic_function.age_results_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
		    else if(func.equals("get_year_results")) 
			{
				 JSONObject receipt_json = statistic_function.year_results_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
		    else if(func.equals("get_month_results"))
			{
				//json_info = {'results_year': year, 'results_month': month, 'results_num': num}
				JSONObject receipt_json1 = statistic_function.month2019_results_fuction();
				JSONObject receipt_json2 = statistic_function.month2020_results_fuction();
				JSONArray jsonArray = new JSONArray(); 
				JSONObject return_ob = new JSONObject(); 
				String year1=receipt_json1.getString("results_year");
				String year2=receipt_json2.getString("results_year");
				jsonArray.put(year1);
				jsonArray.put(year2);
				return_ob.put("results_year", jsonArray);
				JSONArray jsonArray1 = new JSONArray(); 
				String month1=receipt_json1.getString("results_month");
				String month2=receipt_json2.getString("results_month");
				jsonArray.put(month1);
				jsonArray.put(month2);
				return_ob.put("results_month", jsonArray1);
				JSONArray jsonArray2 = new JSONArray(); 
				String day1=receipt_json1.getString("results_num");
				String day2=receipt_json2.getString("results_num");
				jsonArray.put(day1);
				jsonArray.put(day2);
				return_ob.put("results_day", jsonArray2);
				System.out.println(return_ob.toString());
				response.getWriter().write(return_ob.toString());
			}
		    else if(func.equals("get_day_results"))
			{
				 JSONObject receipt_json = statistic_function.day_results_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
		    else if(func.equals("get_country_results")) 
			{
				 JSONObject receipt_json = statistic_function.country_results_fuction();
				 response.getWriter().write(receipt_json.toString());
				 
			}
		    else if(func.equals("get_province_results"))
			{
				 JSONObject receipt_json = statistic_function.province_results_fuction(info2python);
				 
				 response.getWriter().write(receipt_json.toString());
				 
			}
		    else if(func.equals( "get_city_results")) 
			{
				 JSONObject receipt_json = statistic_function.city_results_fuction(info2python);
				 System.out.println(receipt_json.toString());
				 response.getWriter().write(receipt_json.toString());
				 
			}
		
		
	}
	protected void getShowProvince (HttpServletRequest request, HttpServletResponse response) throws Exception {
		String json = WebUtils.readJSONString(request);
		System.out.println(json);
        JSONObject jsonObject = new JSONObject(json);
		String func = jsonObject.getString("function");
		String info2python = jsonObject.getString("infoValue");
		if (func .equals("get_province_allnamelist")) //统计分析-》地区-》省-》下拉选项
		{
			 JSONObject receipt_json = statistic_function.get_province_allnamelist_fuction();
			 response.getWriter().write(receipt_json.toString());
		}
		else if (func .equals("get_area_highgrade")) //地区预警-》高风险地区
		{
			 JSONObject receipt_json = district_warning_function.area_highgrade_fuction();
			 response.getWriter().write(receipt_json.toString());
		}
		else if (func .equals("get_area_midgrade")) //地区预警-》中风险地区
		{
			 JSONObject receipt_json = district_warning_function.area_midgrade_fuction();
			 response.getWriter().write(receipt_json.toString());
		}
	}
	protected void getShowCity (HttpServletRequest request, HttpServletResponse response) throws Exception {
		String json = WebUtils.readJSONString(request);
        JSONObject jsonObject = new JSONObject(json);
		String func = jsonObject.getString("function");
		String info2python = jsonObject.getString("infoValue");
		if (func .equals("get_city_allnamelist")) //统计分析-》地区-》市-》下拉选项
		{
			 JSONObject receipt_json = statistic_function.get_city_allnamelist_fuction();//统计分析-》地区-》市-》下拉选项了
			 response.getWriter().write(receipt_json.toString());
		}
	}
}
