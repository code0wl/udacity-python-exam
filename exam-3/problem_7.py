class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, route):
        self.children[route] = RouteTrieNode()


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, paths, handler):
        node = self.root

        for path in paths:
            if path not in node.children:
                node.children[path] = RouteTrieNode()
            node = node.children[path]

        node.handler = handler

    def find(self, paths):
        node = self.root

        print(paths)

        for path in paths:
            if path not in node.children:
                return None
            node = node.children[path]

        return node.handler


class Router:
    def __init__(self, handler, not_found_handler="404"):
        self.routes = RouteTrie()
        self.routes.insert("/", handler)
        self.not_found = not_found_handler

    def add_handler(self, route, handler):
        paths = self.normalize_url_path(route)
        self.routes.insert(paths, handler)

    def lookup(self, route):
        paths = self.normalize_url_path(route)
        return self.routes.find(paths) or self.not_found

    def normalize_url_path(self, route):
        if len(route) == 1:
            return ["/"]
        else:
            return route.strip("/").split("/")


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))
# should print 'not found handler' or None if you did not implement one
