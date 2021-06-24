<#assign APP_TASK_NAME_STR = "${APP_NAME}">
<#assign APP_TASK_NAME = APP_TASK_NAME_STR?eval>
/*******************************************************************************
  MPLAB Harmony Application Source File

  Company:
    Microchip Technology Inc.

  File Name:
    ${APP_TASK_NAME?lower_case}.c

  Summary:
    This file contains the source code for the MPLAB Harmony application.

  Description:
    This file contains the source code for the MPLAB Harmony application.  It
    implements the logic of the application's state machine and it may call
    API routines of other MPLAB Harmony modules in the system, such as drivers,
    system services, and middleware.  However, it does not call any of the
    system interfaces (such as the "Initialize" and "Tasks" functions) of any of
    the modules in the system or make any assumptions about when those functions
    are called.  That is the responsibility of the configuration-specific system
    files.
 *******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "${APP_TASK_NAME?lower_case}.h"
#include "system/net/sys_net.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************

SYS_MODULE_OBJ      g_netSysServHandle = SYS_MODULE_OBJ_INVALID;

// *****************************************************************************
/* Application Data

  Summary:
    Holds application data

  Description:
    This structure holds the application's data.

  Remarks:
    This structure should be initialized by the ${APP_TASK_NAME?upper_case}_Initialize function.

    Application strings and buffers are be defined outside this structure.
*/

${APP_TASK_NAME?upper_case}_DATA ${APP_TASK_NAME?lower_case}Data;

// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Functions
// *****************************************************************************
// *****************************************************************************

/* TODO:  Add any necessary callback functions.
*/
void netSysServCallback(uint32_t event, void *data, void* cookie)
{
    switch(event)
    {
        case SYS_NET_EVNT_CONNECTED:
        {
			/*
            ** SYS_CONSOLE_PRINT("netSysServCallback(): Status UP\r\n");
			*/
            break;
        }

        case SYS_NET_EVNT_DISCONNECTED:
        {
			/*
            ** SYS_CONSOLE_PRINT("netSysServCallback(): Status DOWN\r\n");
			*/
            break;
        }

        case SYS_NET_EVNT_RCVD_DATA:
        {
			/*
            ** char networkBuffer[256];
            ** memset(networkBuffer, 0, sizeof (networkBuffer));
            ** SYS_NET_RecvMsg(g_tcpSrvcHandle, (uint8_t*) networkBuffer, sizeof (networkBuffer));
			*/
            break;
        }

        case SYS_NET_EVNT_SSL_FAILED:
        {
			/*
            ** SYS_CONSOLE_PRINT("netSysServCallback(): SSL Negotiation Failed\r\n");
            */
			break;
        }

        case SYS_NET_EVNT_DNS_RESOLVE_FAILED:
        {
            /*
			** SYS_CONSOLE_PRINT("netSysServCallback(): DNS Resolution Failed\r\n");
            */
			break;
        }

        case SYS_NET_EVNT_SOCK_OPEN_FAILED:
        {
            /*
			** SYS_CONSOLE_PRINT("netSysServCallback(): Socket Open Failed\r\n");
			*/
            break;
        }
    }
}


// *****************************************************************************
// *****************************************************************************
// Section: Application Local Functions
// *****************************************************************************
// *****************************************************************************


/* TODO:  Add any necessary local functions.
*/


// *****************************************************************************
// *****************************************************************************
// Section: Application Initialization and State Machine Functions
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
  Function:
    void ${APP_TASK_NAME?upper_case}_Initialize ( void )

  Remarks:
    See prototype in ${APP_TASK_NAME?lower_case}.h.
 */

void ${APP_TASK_NAME?upper_case}_Initialize ( void )
{
    /* Place the App state machine in its initial state. */
    ${APP_TASK_NAME?lower_case}Data.state = ${APP_TASK_NAME?upper_case}_STATE_INIT;



    /* TODO: Initialize your application's state machine and other
     * parameters.
     */
    g_netSysServHandle = SYS_NET_Open(NULL, netSysServCallback, 0); 
    if(g_netSysServHandle != SYS_MODULE_OBJ_INVALID)
        SYS_CONSOLE_PRINT("TCP Service Initialized Successfully\r\n");
}


/******************************************************************************
  Function:
    void ${APP_TASK_NAME?upper_case}_Tasks ( void )

  Remarks:
    See prototype in ${APP_TASK_NAME?lower_case}.h.
 */

void ${APP_TASK_NAME?upper_case}_Tasks ( void )
{

    /* Check the application's current state. */
    switch ( ${APP_TASK_NAME?lower_case}Data.state )
    {
        /* Application's initial state. */
        case ${APP_TASK_NAME?upper_case}_STATE_INIT:
        {
			/*
			** TODO: Implement the Task State Machine
			** ${APP_TASK_NAME?lower_case}Data.state = ${APP_TASK_NAME?upper_case}_STATE_SERVICE_TASKS;
			*/
            break;
        }

		/*
		** TODO: Implement various cases/ states for the Application
        case ${APP_TASK_NAME?upper_case}_STATE_SERVICE_TASKS:
        {

            break;
        }
		*/

        /* TODO: implement your application state machine.*/


        /* The default state should never be executed. */
        default:
        {
            /* TODO: Handle error in application's state machine. */
            break;
        }
    }

	SYS_CMD_READY_TO_READ();
	SYS_NET_Task(g_netSysServHandle);
}


/*******************************************************************************
 End of File
 */
