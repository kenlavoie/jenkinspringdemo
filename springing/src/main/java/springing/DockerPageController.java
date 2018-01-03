package springing;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class DockerPageController {

    @RequestMapping("/docker")
    public String index(@RequestParam(value="container", required=true, defaultValue="moby/imaghere") String name, Model model) {
        model.addAttribute("name", name);
        return "greeting";
    }

}
