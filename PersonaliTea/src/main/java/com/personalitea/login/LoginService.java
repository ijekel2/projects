package com.personalitea.login;

/**
 * Created by nathanjekel on 1/30/18.
 */
public class LoginService {

    public boolean isValidUser(String user, String password) {
        if(password.equals("password")) {
            return true;
        }
        return false;
    }
}
