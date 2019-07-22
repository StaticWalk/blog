Java后台中，当需要HTTP请求其他网络资源   
Apache的HttpClient、开源库如OkHttp、原生的HttpURLConnection  
Spring生态中使用RestTemplate来发起HTTP请求
```angular2
// get 请求
//如果只关心返回结果用这个
public <T> T getForObject(); 
//将返回的对象用ResponseEntity封装起来
public <T> ResponseEntity<T> getForEntity();

// head 请求
public HttpHeaders headForHeaders();

// post 请求
public URI postForLocation();
public <T> T postForObject();
public <T> ResponseEntity<T> postForEntity();

// put 请求
public void put();

// pathch 
public <T> T patchForObject

// delete
public void delete()

// options
public Set<HttpMethod> optionsForAllow

// exchange
public <T> ResponseEntity<T> exchange()

```