package com.example.login_n_reg;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Login extends AppCompatActivity {

    EditText e1,e2;
    Button b1;
    DatabaseHelper db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        db=new DatabaseHelper(this);
        e1=(EditText)findViewById(R.id.email2);
        e2=(EditText)findViewById(R.id.pass2);
        b1=(Button)findViewById(R.id.button3);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email=e1.getText().toString();
                String password=e2.getText().toString();
                Boolean chkep=db.emailpass(email,password);
                if(chkep==true){
                    Intent i=new Intent(Login.this,Prediction.class);
                    startActivity(i);
                }
                else {
                    Toast.makeText(getApplicationContext(),"invalid email or password",Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
