local Player = game.Players.LocalPlayer
local Character = Player.Character or Player.CharacterAdded:Wait()
local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")

local speed = 50 -- Tốc độ bay
local flying = false -- Mặc định là không bay

-- Tạo GUI cho Start và Stop
local ScreenGui = Instance.new("ScreenGui")
ScreenGui.Parent = Player.PlayerGui

local StartButton = Instance.new("TextButton")
StartButton.Parent = ScreenGui
StartButton.Size = UDim2.new(0, 200, 0, 50)
StartButton.Position = UDim2.new(0.5, -100, 0.5, -25)
StartButton.Text = "Start Flying"
StartButton.BackgroundColor3 = Color3.fromRGB(0, 255, 0)

local StopButton = Instance.new("TextButton")
StopButton.Parent = ScreenGui
StopButton.Size = UDim2.new(0, 200, 0, 50)
StopButton.Position = UDim2.new(0.5, -100, 0.5, 25)
StopButton.Text = "Stop Flying"
StopButton.BackgroundColor3 = Color3.fromRGB(255, 0, 0)

-- Tạo BodyGyro và BodyVelocity
local bodyGyro = Instance.new("BodyGyro", HumanoidRootPart)
local bodyVelocity = Instance.new("BodyVelocity", HumanoidRootPart)

bodyGyro.P = 9e4
bodyGyro.MaxTorque = Vector3.new(9e4, 9e4, 9e4)
bodyGyro.CFrame = HumanoidRootPart.CFrame

bodyVelocity.MaxForce = Vector3.new(9e4, 9e4, 9e4)
bodyVelocity.Velocity = Vector3.zero

-- Hàm bắt đầu bay
local function startFlying()
    flying = true
    StartButton.Visible = false
    StopButton.Visible = true
end

-- Hàm dừng bay
local function stopFlying()
    flying = false
    bodyVelocity.Velocity = Vector3.zero
    StartButton.Visible = true
    StopButton.Visible = false
end

-- Sự kiện khi nhấn nút Start
StartButton.MouseButton1Click:Connect(function()
    startFlying()
end)

-- Sự kiện khi nhấn nút Stop
StopButton.MouseButton1Click:Connect(function()
    stopFlying()
end)

-- Ẩn nút Stop khi bắt đầu
StopButton.Visible = false

-- Hàm xử lý bay
game:GetService("RunService").RenderStepped:Connect(function()
    if flying then
        local direction = Vector3.zero
        
        -- Di chuyển dựa trên góc nhìn camera
        direction = direction + workspace.CurrentCamera.CFrame.LookVector

        bodyVelocity.Velocity = direction * speed
        bodyGyro.CFrame = workspace.CurrentCamera.CFrame
    end
end)
