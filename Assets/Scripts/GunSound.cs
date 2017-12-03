﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GunSound : MonoBehaviour
{
    AudioSource audioSource;
    void Start()
    {
        audioSource = GetComponent<AudioSource>();
    }

    void Update ()
    {
		if (Input.GetMouseButtonDown(0))
        {
            audioSource.Play();
        }
	}
}
