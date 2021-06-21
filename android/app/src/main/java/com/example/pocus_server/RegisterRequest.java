package com.example.pocus_server;

import com.android.volley.AuthFailureError;
import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class RegisterRequest extends StringRequest {
    final static private String URL = "http://qazx1110.dothome.co.kr/Register.php";
    private Map<String, String> map;


    public RegisterRequest(String userID, String userPassword, String userName, int userStuid, Response.Listener<String> listener) {
        super(Method.POST, URL, listener, null);

        map = new HashMap<>();
        map.put("userId", userID);
        map.put("userPassword", userPassword);
        map.put("userName", userName);
        map.put("userStuid", userStuid + "");
    }

    @Override
    protected Map<String, String> getParams() throws AuthFailureError {
        return map;
    }

}
