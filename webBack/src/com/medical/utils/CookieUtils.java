package com.medical.utils;

import javax.servlet.http.Cookie;

public class CookieUtils {
	public static Cookie findCookie(String name,Cookie[]cookies) {
		if(name==null||cookies==null||cookies.length==0)
			return null;
		for(Cookie cookie:cookies) {
			if(name.equals(cookie))
				return cookie;
		}
		return null;
	}
}
