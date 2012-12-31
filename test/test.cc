
// The Comment will not parse.
// [[Helper default] commIncreaseDataCollect:@"Device_Type" key:@"iPhone4"];

/*
[[Helper default] commIncreaseDataCollect:@"Device_Type" key:@"iPhone4"];
*/

NSString *key = @"iOS_6.0";

[[Helper default] commIncreaseDataCollect:@"Device_Type" key:@"iPhone4"];

NSString *target = @"Device_Type";

[[Helper default] commIncreaseDataCollect:target key:@"iPhone4"];

[[Helper default] commIncreaseDataCollect:@"iOS_Version" key:key];

[[Helper default] commIncreaseDataCollect:@"WrongTargetName_" key:@"rightKey"];

[[Helper default] commIncreaseDataCollect:@"RightTargetName" key:@"wrongKey_"];

NSString *varTarget_ = @"varTarget"
NSString *varKey_ = @"varKey"

[[Helper default] commIncreaseDataCollect:varTarget_ key:varKey_];