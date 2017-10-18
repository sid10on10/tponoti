package me.zeroonehacker.www.tponoti;

import android.util.Log;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.iid.FirebaseInstanceIdService;

/**
 * Created by zeroonehacker on 15/10/17.
 */

public class MyFirebaseInstanceIDService extends FirebaseInstanceIdService {
    private static final String TAG = "MyFirebaseIIDService";
    @Override
    public void onTokenRefresh() {
        String refreshedToken = FirebaseInstanceId.getInstance().getToken();
        Log.d(TAG, "Token : " + refreshedToken);
        
        storeToken(refreshedToken);
    }

    private void storeToken(String refreshedToken) {
        SharedPrefManager.getInstance(getApplicationContext()).saveDeviceToken(refreshedToken);
    }
}
