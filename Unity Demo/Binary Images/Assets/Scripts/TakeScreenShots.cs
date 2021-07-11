using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TakeScreenShots : MonoBehaviour
{
    [SerializeField] GameObject target;
    [SerializeField] Material whiteMaterial;
    private Renderer[] materials;

    // Start is called before the first frame update
    void Start()
    {
        materials = target.GetComponentsInChildren<Renderer>();
        foreach (Renderer renderer in materials)
        {
            renderer.material = whiteMaterial;
        }

        ScreenCapture.CaptureScreenshot(Application.dataPath + "/Images/Test.jpg");
    }
}
