<#if HarmonyCore.SELECT_RTOS == "FreeRTOS">
<#lt>static void _SYS_OTA_Tasks(  void *pvParameters  )
<#lt>{
<#lt>    while(1)
<#lt>    {
<#lt>        SYS_OTA_Tasks();
         <#if OTA_RTOS_TASK_DELAY gt 0>
<#lt>        vTaskDelay(${OTA_RTOS_TASK_DELAY}/ portTICK_PERIOD_MS);
         </#if>
<#lt>    }
<#lt>}
<#lt>
</#if>