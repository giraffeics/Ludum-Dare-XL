﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletDestroy : MonoBehaviour {

	// Use this for initialization
	void Start ()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (gameObject.name == "Bullet(Clone)")
        {
            Destroy(gameObject, 2.50f);
        }
    }
}
