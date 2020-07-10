package com.medical.service;

import com.medical.entity.User;

public interface UserService {
	public void registUser(User user);
	public User login(User user);
	public boolean existsUsername(String username);
}
