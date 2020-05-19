package com.example.login_n_reg;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.app.Activity;
import android.app.VoiceInteractor;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.HttpHeaderParser;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class Prediction extends Activity {

    EditText e1,e2,e3,e4,e5,e6;
    TextView result;
    Button p;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_prediction);

        e1=(EditText)findViewById(R.id.symptom1);
        e2=(EditText)findViewById(R.id.symptom2);
        e3=(EditText)findViewById(R.id.symptom3);
        e4=(EditText)findViewById(R.id.symptom4);
        e5=(EditText)findViewById(R.id.symptom5);
        e6=(EditText)findViewById(R.id.symptom6);
        p=(Button)findViewById(R.id.predict);


        result=(TextView)findViewById(R.id.result);
        final RequestQueue requestQueue = Volley.newRequestQueue(this);
        p.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String s1 = e1.getText().toString();
                String s2 = e2.getText().toString();
                String s3 = e3.getText().toString();
                String s4 = e4.getText().toString();
                String s5 = e5.getText().toString();
                String s6 = e6.getText().toString();
                String s = s1;
                s=s.concat(",");s=s.concat(s2);s=s.concat(",");s=s.concat(s3);s=s.concat(",");s=s.concat(s4);s=s.concat(",");s=s.concat(s5);s=s.concat(",");s=s.concat(s6);
               // s += "," + s2;
               // s += "," + s3;
                //s += "," + s4;
              //  s += "," + s5;
                //s += "," + s6;
                System.out.println(s);

                //try {
                //    String url = "http://13.127.24.110:8000/dPredictor/";

                    // Gson gson=new Gson();
                    // String json=gson.toJson(s);


                    //JsonParser parser=new JsonParser();
                    //String t=parser.parse(s).getAsString();

                   /* JsonObjectRequest jsonObjReq= new JsonObjectRequest(Request.Method.POST, url, jsonBody, new Response.Listener<JSONObject>() {
                        @Override
                        public void onResponse(JSONObject response) {
                            try {
                                if (response.getBoolean("status")) {
                                    result.setText(response.toString());
                                    Toast.makeText(getApplicationContext(), "Take Care", Toast.LENGTH_SHORT).show();
                                }
                            }catch (JSONException e){
                                e.printStackTrace();
                            }
                        }
                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            error.printStackTrace();
                            Toast.makeText(getApplicationContext(), "can't connect to server", Toast.LENGTH_SHORT).show();
                        }
                    });
                    JsonArray jsonBody=new JsonArray();
                    jsonBody.add(s);
                    final String requestBody=jsonBody.toString();
                    */
                    //JSONObject jsonBody = new JSONObject("\""+s+"\"");
                    //final String requestBody = jsonBody.toString();
                    /*JSONArray jsonBody=new JSONArray();
                    jsonBody.put(s1);
                    jsonBody.put(s2);
                    jsonBody.put(s3);
                    jsonBody.put(s4);
                    jsonBody.put(s5);
                    jsonBody.put(s6);
                    final String requestBody = jsonBody.toString();
                    System.out.println(requestBody);
                   /* StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            result.setText(response.toString());
                            Toast.makeText(getApplicationContext(), response.toString(), Toast.LENGTH_SHORT).show();
                        }
                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            error.printStackTrace();
                        }
                    }){
                    @Override
                    public String getBodyContentType () {
                        return "application/json; charset=utf-8";
                    }
                    @Override
                    public byte[] getBody () throws AuthFailureError {
                        try {
                            return requestBody==null ? null : requestBody.getBytes("utf-8");
                        } catch (UnsupportedEncodingException uee) {
                            VolleyLog.wtf("Unsupported Encoding while trying to get the bytes of %s using %s", requestBody, "utf-8");
                            return null;
                        }
                    }


                    @Override
                    protected Response<String> parseNetworkResponse (NetworkResponse response){
                        String responseString = "";
                        if (response != null) {
                            responseString = String.valueOf(response.statusCode);
                            // can get more details such as response.headers
                        }
                        return Response.success(responseString, HttpHeaderParser.parseCacheHeaders(response));
                    }
                };
                    requestQueue.add(stringRequest);
                }catch (Exception e){
                    String t="can not connect to server";
                    result.setText(t);
                    e.printStackTrace();
                }*/



                try {
                    //JSONObject para = new JSONObject(s.substring(0,s.length()-1));
                    JSONArray jsonBody=new JSONArray();
                    jsonBody.put(s1);
                    jsonBody.put(s2);
                    jsonBody.put(s3);
                    jsonBody.put(s4);
                    jsonBody.put(s5);
                    jsonBody.put(s6);

                    //final String requestBody = jsonBody.toString();
                    HashMap<String,JSONArray> params= new HashMap<String,JSONArray>();
                    params.put("array",jsonBody);
                    //JSONObject obj=new JSONObject();
                    //obj.put("array",jsonBody);
                    System.out.println(params);

                    String url = "http://13.127.24.110:8000/dPredictor/";
                    JsonObjectRequest request = new JsonObjectRequest(Request.Method.POST, url, new JSONObject(params),
                            new Response.Listener<JSONObject>() {
                                @Override
                                public void onResponse(JSONObject response) {
                                    result.setText(response.toString());
                                    Toast.makeText(getApplicationContext(), "Take Care", Toast.LENGTH_SHORT).show();

                                }
                            }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            error.printStackTrace();
                            Toast.makeText(getApplicationContext(), "can't connect to server", Toast.LENGTH_SHORT).show();
                        }
                    });
                    requestQueue.add(request);
                } catch (Exception e) {
                    e.printStackTrace();
                }

            }
        });
    }
}
