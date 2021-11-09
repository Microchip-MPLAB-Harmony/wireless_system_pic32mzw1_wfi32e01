<#if HarmonyCore.SELECT_RTOS == "FreeRTOS">
<#lt>static void _SYS_WSS_Task(  void *pvParameters  )
<#lt>{
<#lt>    while(1)
<#lt>    {
<#lt>        SYS_WSS_Task(sysObj.sysWSS);
         <#if SYS_WSS_RTOS_TASK_DELAY gt 0>
<#lt>        vTaskDelay(${SYS_WSS_RTOS_TASK_DELAY}/ portTICK_PERIOD_MS);
         </#if>
<#lt>    }
<#lt>}
<#lt>
</#if>