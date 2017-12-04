﻿using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Health : MonoBehaviour
{
    private float startingHealth = 100.00f;
    private float currentHealth;
    private float decreaseTime = 1.50f;
    public Camera cam;
    //public Text test;
    public Material highlight;
    public Material norm;
    public Slider healthBar;
    private bool soundPlayed = false;

    private GameObject cerealParent = null;
    private GameObject cerealChild = null;
    private bool cerealExists = false;

    void Start()
    {
        currentHealth = startingHealth;
        healthBar.value = CalcHealth();
    }

    void Update()
    {
        if (cerealExists)
        {
            try
            {
                cerealChild.GetComponent<Renderer>().material = norm;
            }
            catch (Exception e)
            {
                cerealExists = false;
            }
        }

        Vector3 rayOrigin = cam.ViewportToWorldPoint(new Vector3(0, 0, 0));
        Vector3 fwd = transform.TransformDirection(Vector3.forward);
        int layerMask = 1 << 8;

        RaycastHit hit;

        if (Physics.Raycast(rayOrigin, fwd, out hit, 2, layerMask))
        {
            cerealParent = hit.transform.gameObject;
            cerealChild = hit.transform.GetChild(0).gameObject;

            if (cerealExists == false)
            {
                cerealParent.GetComponent<HighlightSound>().PlayHLSound();
                //soundPlayed = true;
            }

            cerealExists = true;

            //Debug.DrawRay(rayOrigin, fwd, Color.green);
            cerealChild.GetComponent<Renderer>().material = highlight;

            if (Input.GetKey("e"))
            {
                Destroy(cerealParent);
                cerealExists = false;
                AddHealth();
            }
        }
        else
            cerealExists = false;

        //soundPlayed = false;

        if (currentHealth == 0)
        {
            Die();
        }

        if (currentHealth > 100)
        {
            currentHealth = 100;
        }

        if (currentHealth < 0)
        {
            currentHealth = 0;
        }

        currentHealth -= decreaseTime * Time.deltaTime;
        healthBar.value = CalcHealth();
        //test.text = "" + currentHealth;

    }

    float CalcHealth()
    {
        return currentHealth / startingHealth;
    }

    public void AddHealth()
    {
        currentHealth += 20.00f;
        healthBar.value = CalcHealth();
    }

    public void LoseHealth()
    {
        currentHealth -= 10.00f;
        healthBar.value = CalcHealth();
    }

    void Die()
    {
        Debug.Log("You died!");
    }
}